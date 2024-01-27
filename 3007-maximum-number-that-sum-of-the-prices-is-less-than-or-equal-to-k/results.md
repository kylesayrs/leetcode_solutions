This algorithm is understandable, although it is slow O(k).

The faster approach notices that, for any range of numbers `n``, the number of
set bits in the `i`th place follows a repeating pattern. There is therefore
a closed form equation which decribes the sum of the number of set bits up to `n`
for the `i`th place. This means it takes O(i) time to calculate the sum of prices
up to `n`, which allows you to do an efficient binary search for the correct `n`
value.

Maybe I'll implement this later, but since I'm still learning rust, I'm pretty
happy with my solution and that I learned more about bit manipulation in Rust.
