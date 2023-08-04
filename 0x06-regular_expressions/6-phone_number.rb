#!/usr/bin/env ruby
#Matches 10digits phone number
#puts ARGV[0].scan(/\d{10,10}/).join
puts ARGV[0].scan(/^\d{10,10}$/).join
