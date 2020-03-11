
whitepages = File::binread("whitepages.txt")
#print whitepages
output = ''
binstring = ''
for a in 0..whitepages.length-1
  ch = whitepages[a].ord
  if ch == 32
    binstring += "1"
  #elsif ch == 128
    #binstring += "10"
  #elsif ch == 131
    #binstring += "01"
  elsif ch == 226
    binstring += "0"
  else
    #print "wat #{ch}"
  end
  if binstring.length == 8
    num = binstring.to_i(2)
    output += num.chr
    binstring = ''
  end
end
print output

File::binwrite("whitepages.dec", output)

