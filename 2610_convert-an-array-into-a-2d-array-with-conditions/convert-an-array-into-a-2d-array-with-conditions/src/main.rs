use std::collections::HashMap;

struct Solution {}

impl Solution {
    fn insert_into_matrix(matrix: &mut Vec<Vec<i32>>, row: usize, value: i32) {
        let num_rows_to_append: i32 = row as i32 - matrix.len() as i32 + 1;

        if num_rows_to_append > 0 {
            for _ in 0..num_rows_to_append {
                matrix.push(vec![]);
            }
        }

        matrix[row].push(value);
    }

    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut matrix: Vec<Vec<i32>> = vec![];

        let mut freqencies: HashMap<i32, usize> = HashMap::new();

        for num in nums {
            let frequency = match freqencies.get(&num) {
                Some(&frequency) => frequency,
                None => 0,
            };

            Solution::insert_into_matrix(&mut matrix, frequency, num);
            freqencies.insert(num, frequency + 1);
        }
        
        matrix
    }
}

fn main() {
    println!("{:?}", Solution::find_matrix(vec![1, 1, 1, 3, 2, 1]));
}
