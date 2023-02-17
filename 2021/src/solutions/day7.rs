fn part1(numbers: &Vec<i32>) -> i32{
    let median: i32 = numbers[numbers.iter().len()/2];
    let cost: i32 = numbers.iter()
        .map(|x| (median - x).abs())
        .sum();
    cost
}

fn part2(lines: &Vec<i32>) -> i32 {
    0
}

pub(crate) fn solve(input: &str) -> (String, String){
    let mut numbers: Vec<i32> = input.split(",")
        .map(|x| x.parse::<i32>().unwrap_or(0))
        .collect();
    numbers.sort();
    (part1(&numbers).to_string(), part2(&numbers).to_string())
}