percentage = 0.03
years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuition = 20_000

years.each do |_year|
  tuition += tuition * percentage
  puts "In year #{years[_year]} the tuition will be #{tuition}"
end
