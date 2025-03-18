function filtered_signal = wiener_filter(input_signal)
    filtered_signal = wiener2(input_signal, [5 5]);
end
