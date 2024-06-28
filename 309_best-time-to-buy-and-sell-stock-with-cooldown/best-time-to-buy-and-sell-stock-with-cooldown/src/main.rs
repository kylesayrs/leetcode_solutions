#![allow(unused_parens)]

struct DefaultCache<T> {
    rows: usize,
    columns: usize,
    cache: Vec<Vec<T>>,
    default: T
}

impl<T: std::clone::Clone> DefaultCache<T> {
    pub fn new(rows: usize, columns: usize, default: T) -> Self {
        DefaultCache {
            rows: rows,
            columns: columns,
            cache: vec![vec![default; columns]; rows],
            default: default
        }
    }
}

impl<T: std::clone::Clone> std::ops::Index<(usize, usize)> for DefaultCache<T> {
    type Output = T;

    fn index(&self, idx: (usize, usize)) -> &T {
        if (
            idx.0 < 0 || idx.0 > self.rows ||
            idx.1 < 0 || idx.1 > self.columns
        ) {
            &self.default
        } else {
            &self.cache[idx.0][idx.1]
        }
    }
}

impl<T: std::clone::Clone> std::ops::IndexMut<(usize, usize)> for DefaultCache<T> {
    fn index_mut(&mut self, idx: (usize, usize)) -> &mut T {
        if (
            idx.0 < 0 || idx.0 > self.rows ||
            idx.1 < 0 || idx.1 > self.columns
        ) {
            self.default.clone().into_mut()
        } else {
            &mut self.cache[idx.0][idx.1]
        }
    }
}



struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        0
    }
}

fn main() {
    println!("Hello, world!");
}


#[test]
fn test_default_cache() {
    //let mut cache = DefaultCache::new(2, 2, -1);
    //cache[(0, 0)] = 1;
    //assert_eq!(cache[(0, 0)], 1);
    let vec = vec![1, 2, 3];
    
}
