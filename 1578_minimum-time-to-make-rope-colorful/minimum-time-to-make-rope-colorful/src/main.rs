struct Solution {}

impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        if colors.len() <= 0 {
            return 0;
        }

        let color_chars = colors.chars().collect::<Vec<char>>();
        
        let mut max_time_for_color = needed_time[0];
        let mut current_color = color_chars[0];
        let mut total_needed_time = 0;

        for index in 1..colors.len() {
            if current_color != color_chars[index] {
                max_time_for_color = needed_time[index];
                current_color = color_chars[index];
                continue;
            }

            if needed_time[index] > max_time_for_color {
                total_needed_time += max_time_for_color;
                max_time_for_color = needed_time[index];
                
            } else {
                total_needed_time += needed_time[index];
            }
        }

        total_needed_time
    }
}


fn main() {
    println!("{:?}", Solution::min_cost(String::from("aaabcaccc"), vec![5, 20, 1, 2, 3, 10, 2, 3, 1]));
}
