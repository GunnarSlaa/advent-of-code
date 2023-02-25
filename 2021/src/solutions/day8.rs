const LENGTHS: [usize; 4] = [2,3,4,7];

fn part1(lines: &Vec<&str>) -> i32{
    let mut count = 0;
    for line in lines{
        let output = line.split(" | ").collect::<Vec<&str>>()[1];
        count += output.split(' ')
            .filter(|x| LENGTHS.contains(&x.len()))
            .collect::<Vec<&str>>().len()
    }
    count as i32
}

fn part2(lines: &Vec<&str>) -> i32{
    0
}

pub(crate) fn solve(input: &str) -> (String, String){
    let lines: Vec<&str> = input.split("\r\n")
        .collect();
    (part1(&lines).to_string(), part2(&lines).to_string())
}