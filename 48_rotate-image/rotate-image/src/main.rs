mod solution;

fn main() {
    let mut image3x3: Vec<Vec<i32>> = vec![
        vec![1, 2, 3],
        vec![4, 5, 6],
        vec![7, 8, 9],
    ];
    println!("image: {:?}", image3x3);
    
    solution::Solution::rotate(&mut image3x3);
    println!("rotated image: {:?}", image3x3);
}
