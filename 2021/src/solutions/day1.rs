use super::*;

fn part1(lines: &[u32]) -> u32{
    let mut previous = &lines[0];
    let mut count = 0;
    for (c, num) in lines.iter().enumerate(){
        if c == 0 {continue;}
        if num > previous {count+=1;}
        previous = num;
    }
    count
}

fn part2(lines: &[u32]) -> u32{
    let mut previous = lines[0] + lines[1] + lines[2];
    let mut count = 0;
    for c in 1..lines.len() {
        if c < 2 {continue;}
        let sum = lines[c - 2] + lines[c - 1] + lines[c];
        if sum > previous {count+=1;}
        previous = sum;
    }
    count
}

pub(crate) fn solve(input: &str) -> (String, String){
    let lines: Vec<u32> = to_nums::<u32>(input, "\r\n").unwrap_or(Vec::new());
    (part1(&lines).to_string(), part2(&lines).to_string())
}