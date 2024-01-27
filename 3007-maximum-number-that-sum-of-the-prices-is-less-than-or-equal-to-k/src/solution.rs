pub struct Solution {}

impl Solution {
    pub fn find_maximum_number(k: i64, x: i32) -> Result<i64, &'static str> {
        if k < 1 || x < 1 {
            return Err("Bad input")
        }

        let price_bit_mask = Solution::get_price_bit_mask(x);

        let mut price_sum = 0;
        let mut max_num: i64 = 1;
        for num in 1.. {
            let price = Solution::bk_sum_bits(num & price_bit_mask);
            price_sum += price;
            
            if price_sum > k {
                max_num = (num - 1) as i64;
                break;
            }
        }

        return Ok(max_num);
    }

    pub fn get_price_bit_mask(x: i32) -> u32 {
        assert!(x > 0);

        let mut bit_mask: u32 = 0;
        for i in (0..33).step_by(x as usize) {
            if i == 0 { continue }
            bit_mask |= 1u32 << (i - 1);
        }

        return bit_mask;
    }

    fn bk_sum_bits(num: u32) -> i64 {
        let mut num_copy = num;

        let mut count = 0;
        while num_copy != 0 {
            num_copy &= num_copy - 1;
            count += 1;
        }

        return count;
    }
}


/* Unit tests */


#[test]
fn test_error() {
    match Solution::find_maximum_number(0, 0) {
        Err(_) => assert!(true),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(1, 0) {
        Err(_) => assert!(true),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(0, 1) {
        Err(_) => assert!(true),
        _ => assert!(false)
    }
}


#[test]
fn test_basic_ones() {
    match Solution::find_maximum_number(1, 1) {
        Ok(max_num) => assert_eq!(max_num, 1),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(2, 1) {
        Ok(max_num) => assert_eq!(max_num, 2),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(3, 1) {
        Ok(max_num) => assert_eq!(max_num, 2),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(4, 1) {
        Ok(max_num) => assert_eq!(max_num, 3),
        _ => assert!(false)
    }
}


#[test]
fn test_basic_twos() {
    match Solution::find_maximum_number(1, 2) {
        Ok(max_num) => assert_eq!(max_num, 2),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(2, 2) {
        Ok(max_num) => assert_eq!(max_num, 5),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(3, 2) {
        Ok(max_num) => assert_eq!(max_num, 6),
        _ => assert!(false)
    }
}


#[test]
fn test_leetcode() {
    match Solution::find_maximum_number(9, 1) {
        Ok(max_num) => assert_eq!(max_num, 6),
        _ => assert!(false)
    }

    match Solution::find_maximum_number(7, 2) {
        Ok(max_num) => assert_eq!(max_num, 9),
        _ => assert!(false)
    }
}


#[test]
fn test_get_price_bit_mask() {
    assert_eq!(Solution::get_price_bit_mask(1), 0b11111111111111111111111111111111);
    assert_eq!(Solution::get_price_bit_mask(2), 0b10101010101010101010101010101010);
    assert_eq!(Solution::get_price_bit_mask(3), 0b00100100100100100100100100100100);
}
