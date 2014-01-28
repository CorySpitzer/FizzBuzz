class Num
  attr_accessor :val
  attr_accessor :fizz
  attr_accessor :buzz

  def initialize(value)
    @val = value

    if value % 3 == 0
      @fizz = true
    else
      @fizz = false
    end

    if value % 5 == 0
      @buzz = true
    else
      @buzz = false
    end
  end
end

def main()
  nums = []
  (1..100).each do |i|
    nums.push(Num.new(i))
  end

  nums.each do |num|
    if num.fizz and num.buzz
      puts "fizzbuzz"
    elsif num.fizz
      puts "fizz"
    elsif num.buzz
      puts "buzz"
    else
      puts num.val
    end
  end
end

main()
