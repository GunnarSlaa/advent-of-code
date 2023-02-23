use super::*;

fn round(old: [u64; 9]) -> [u64; 9]{
    let mut new = [0;9];
    new[..8].copy_from_slice(&old[1..]);
    new[8] = old[0];
    new[6] += old[0];
    new
}

pub(crate) fn solve(input: &str) -> (String, String){
    let numbers: Vec<usize> = to_nums::<usize>(input, ",").unwrap_or(Vec::new());
    let mut counts: [u64; 9] = [0; 9];
    let mut solution: (u64, u64) = (0,0);
    for number in numbers{
        counts[number] += 1;
    }
    for j in 0..256{
        if j == 80{
            solution.0 = counts.iter().sum::<u64>();
        }
        counts = round(counts);
    }
    solution.1 = counts.iter().sum::<u64>();
    (solution.0.to_string(), solution.1.to_string())
}