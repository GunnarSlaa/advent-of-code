use super::*;

fn part1(numbers: &Vec<i32>) -> i32{
    let median: i32 = numbers[numbers.iter().len()/2];
    numbers.iter()
        .map(|x| (median - x).abs())
        .sum()
}

fn part2(numbers: &Vec<i32>) -> i32 {
    let mut from_left:Vec<i32> = Vec::new();
    let mut total_costs_left:Vec<i32> = Vec::new();
    let mut cost = 0;
    let mut total_cost = 0;
    let mut amount = 0;
    let mini = *numbers.iter().min().unwrap_or(&0);
    let maxi = *numbers.iter().max().unwrap_or(&0) + 1;
    for i in mini..maxi{
        amount += numbers.iter().filter(|&n| *n == i).count() as i32;
        cost += amount;
        total_cost += cost;
        from_left.push(cost);
        total_costs_left.push(total_cost);
    }
    cost = 0;
    amount = 0;
    total_cost = 0;
    for i in (mini..maxi).rev(){
        amount += numbers.iter().filter(|&n| *n == i).count() as i32;
        cost += amount;
        if cost > from_left[i as usize - 1]{
            return total_cost + total_costs_left[i as usize - 1];
        }
        total_cost += cost;
    }
    0
}

pub(crate) fn solve(input: &str) -> (String, String){
    let mut numbers: Vec<i32> = to_nums::<i32>(input, ",").unwrap_or(Vec::new());
    numbers.sort();
    (part1(&numbers).to_string(), part2(&numbers).to_string())
}