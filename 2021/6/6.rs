use std::fs;
use std::env;

fn round(old: [u64; 9]) -> [u64; 9]{
    let mut new = [0;9];
    new[..8].copy_from_slice(&old[1..]);
    new[8] = old[0];
    new[6] += old[0];
    return new;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Can't read file");
    let numbers: Vec<usize> = data.split(",")
        .map(|x| x.parse::<usize>().unwrap_or(0)).collect();
    let mut counts: [u64; 9] = [0; 9];
    for number in numbers{
        counts[number] += 1;
    }
    for j in 0..256{
        if j == 80{
            println!("Part1: {}", counts.iter().sum::<u64>());
        }
        counts = round(counts);
    }
    println!("Part2: {}", counts.iter().sum::<u64>());
}