use std::fs;
use std::convert::TryInto;

fn main() {
    let data = fs::read_to_string("input_test").expect("Can't read file");
    let lines = data.split("\r\n");
    let mut lines_vec: Vec<&str> = lines.clone().collect();
    let mut lines_count = lines_vec.len();
    let line_size = lines_vec[0].len();

    for column in 0..line_size {
        let mut count = 0;
        for line in lines_vec.clone().iter() {
            if &line[column..column + 1] == "1" {count += 1}
        }
        let looking_for = if count > lines_count / 2 {"1"} else {"0"};
        lines_vec = lines_vec.iter().map(|x| if &x[column..column + 1] == looking_for {x}).collect()
    }

    // println!("Gamma: {}", gamma);
    // println!("Epsilon: {}", epsilon);
    // println!("Answer: {}", epsilon * gamma);
}