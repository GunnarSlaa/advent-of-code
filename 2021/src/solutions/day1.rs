fn part1(lines: &Vec<u32>) -> u32{
    let mut previous = &lines[0];
    let mut count = 0;
    for (c, num) in lines.iter().enumerate(){
        if c == 0 {continue;}
        if num > previous {count+=1;}
        previous = num;
    }
    count
}

fn part2(lines: &Vec<u32>) -> u32{
    let mut previous = &lines[0] + &lines[1] + &lines[2];
    let mut count = 0;
    for c in 1..lines.len() {
        if c < 2 {continue;}
        let sum = &lines[c - 2] + &lines[c - 1] + &lines[c];
        if sum > previous {count+=1;}
        previous = sum;
    }
    count
}

pub(crate) fn solve(input: &str) -> (String, String){
    let lines: Vec<u32> = input.clone().split("\r\n").map(|x| x.parse::<u32>().unwrap_or(0)).collect();
    (part1(&lines).to_string(), part2(&lines).to_string())
}