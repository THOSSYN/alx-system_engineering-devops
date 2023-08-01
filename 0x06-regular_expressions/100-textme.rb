#!/usr/bin/env ruby
#Matches phone nos of sender and receiver

sender = ARGV[0].scan(/from:(\+?\w*\s*\w*)/).join
recipient = ARGV[0].scan(/to:(\+?\d+)/).join
flag= ARGV[0].scan(/flags:((:?-?\d){4})/).join

puts "#{sender},#{recipient},#{flag}"
