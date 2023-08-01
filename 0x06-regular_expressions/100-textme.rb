#!/usr/bin/env ruby
#Matches phone nos of sender and receiver

sender = ARGV[0].scan(/\[from:(.*?)\]/).join
recipient= ARGV[0].scan(/\[to:(.*?)\]/).join
flag= ARGV[0].scan(/\[flags:(.*?)\]/).join

puts "#{sender},#{recipient},#{flag}"
