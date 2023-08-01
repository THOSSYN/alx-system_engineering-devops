#!/usr/bin/env ruby

def extract_info(input)
  matches = input.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
  matches.empty? ? nil : matches
end

def print_statistics(matches)
  if matches
    matches.each do |sender, receiver, flags|
      puts "#{sender},#{receiver},#{flags}"
    end
  else
    puts "No matches found."
  end
end

# Extract sender, receiver, and flags
input_string = ARGV[0]
matches = extract_info(input_string)
print_statistics(matches)
