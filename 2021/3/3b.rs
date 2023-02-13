use std::fs;

fn main() {
    let data = fs::read_to_string("input_test").expect("Can't read file");
    let lines = data.split("\r\n");
    let mut lines_vec: Vec<&str> = lines.clone().collect();
    let mut lines_count = lines_vec.len();
    let line_size = lines_vec[0].len();

    for column in 0..line_size {
        let count = lines_vec.clone().into_iter()
            .filter(|x|{&x[column..column + 1] == "1"})
            .collect::<Vec<&str>>()
            .len();
        let looking_for = if count * 2 >= lines_count {"1"} else {"0"};
        lines_vec = lines_vec.into_iter().filter(|x|{&x[column..column + 1] == looking_for}).collect();
        lines_count = lines_vec.len();
        if lines_count == 1 {break;}
    }
    let oxygen_rating = usize::from_str_radix(&lines_vec[0], 2).unwrap();

    lines_vec = lines.clone().collect();
    lines_count = lines_vec.len();
    for column in 0..line_size {
        let count = lines_vec.clone().into_iter()
            .filter(|x|{&x[column..column + 1] == "1"})
            .collect::<Vec<&str>>()
            .len();
        let looking_for = if count * 2 < lines_count {"1"} else {"0"};
        lines_vec = lines_vec.into_iter().filter(|x|{&x[column..column + 1] == looking_for}).collect();
        lines_count = lines_vec.len();
        if lines_count == 1 {break;}
    }
    let co2_scrubber = usize::from_str_radix(&lines_vec[0], 2).unwrap();

    println!("Oxygen rating: {}", oxygen_rating);
    println!("CO2 scrubber rating: {}", co2_scrubber);
    println!("Answer: {}", oxygen_rating * co2_scrubber);
}