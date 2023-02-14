use std::fs;

struct BingoCard{
    numbers: Vec<i32>,
    hit: [i32; 25],
}

fn main() {
    let data = fs::read_to_string("input_test_fake").expect("Can't read file");
    let blocks = data.split("\r\n\r\n");
    let numbers: Vec<i32> = blocks.clone()
        .collect::<Vec<&str>>()[0]
        .split(",")
        .map(|x| x.parse::<i32>().unwrap_or(0))
        .collect();

    // let mut bingo_cards: Vec<BingoCard>;

    for block in &blocks.clone().collect::<Vec<&str>>()[1..] {
        let nums: Vec<i32> = block
            .split([' ', '\r', '\n'])
            .filter(|x| x != &"")
            .map(|x| x.parse::<i32>().unwrap_or(0))
            .collect::<Vec<i32>>();
    }

    println!("{}", numbers.len());
    println!("{}", blocks.collect::<Vec<&str>>().len());
}