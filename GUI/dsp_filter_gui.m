function dsp_filter_gui
    fig = uifigure('Name', 'DSP Noise Reduction & Image Enhancement', 'Position', [100 100 600 500]);

    % Upload Button
    btnUpload = uibutton(fig, 'Text', 'Upload File', 'Position', [50, 420, 120, 30]);
    btnUpload.ButtonPushedFcn = @(btnUpload, event) upload_file();

    % File Type Dropdown (Audio or Image)
    fileTypeDropDown = uidropdown(fig, 'Items', {'Audio', 'Image'}, ...
        'Position', [200, 420, 120, 30]);

    % Filter Selection Drop-Down
    filterDropDown = uidropdown(fig, 'Items', {'Low-Pass', 'High-Pass', 'Wiener Filter', 'Adaptive Contrast'}, ...
        'Position', [350, 420, 120, 30]);

    % Apply Filter Button
    btnApply = uibutton(fig, 'Text', 'Apply Filter', 'Position', [500, 420, 100, 30]);
    btnApply.ButtonPushedFcn = @(btnApply, event) apply_filter(filterDropDown.Value, fileTypeDropDown.Value);

    function upload_file()
        [file, path] = uigetfile({'*.wav;*.jpg;*.png', 'Audio & Images (*.wav, *.jpg, *.png)'});
        if file ~= 0
            global input_data fs fileType;
            fileType = fileTypeDropDown.Value;
            fullFilePath = fullfile(path, file);

            if strcmp(fileType, 'Audio')
                [input_data, fs] = audioread(fullFilePath);
                uialert(fig, 'Audio file uploaded successfully!', 'Success');
            else
                input_data = imread(fullFilePath);
                uialert(fig, 'Image file uploaded successfully!', 'Success');
            end
        end
    end

    function apply_filter(filter_type, file_type)
        global input_data fs fileType;
        if isempty(input_data)
            uialert(fig, 'Upload a file first!', 'Error');
            return;
        end

        if strcmp(file_type, 'Audio')
            % Apply 1D Audio Filtering
            switch filter_type
                case 'Low-Pass'
                    filtered_audio = low_pass_filter(input_data, fs);
                case 'High-Pass'
                    filtered_audio = high_pass_filter(input_data, fs);
                case 'Wiener Filter'
                    filtered_audio = wiener_filter(input_data);
            end
            audiowrite('../data/filtered_output.wav', filtered_audio, fs);
            figure; plot(filtered_audio);
            title(['Filtered Audio - ', filter_type]);

        else
            % Apply 2D Image Filtering
            switch filter_type
                case 'Low-Pass'
                    h = fspecial('average', 5);
                case 'High-Pass'
                    h = fspecial('laplacian', 0.5);
                case 'Adaptive Contrast'
                    h = adapthisteq(input_data);
            end
            filtered_image = imfilter(input_data, h, 'replicate');

            imwrite(filtered_image, '../data/filtered_output.png');
            figure; imshow(filtered_image);
            title(['Filtered Image - ', filter_type]);
        end
    end
end
