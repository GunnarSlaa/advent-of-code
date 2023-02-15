use std::fs;
use std::str::FromStr;

enum InstructionType {
    Forward,
    Down,
    Up,
}

impl FromStr for InstructionType {
    type Err = ();
    fn from_str(input: &str) -> Result<InstructionType, Self::Err>{
        match input {
            "forward"   => Ok(InstructionType::Forward),
            "down"      => Ok(InstructionType::Down),
            "up"        => Ok(InstructionType::Up),
            _           => Err(()),
        }
    }
}

struct Instruction {
    instruction_type: InstructionType,
    amount: i32,
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let data = fs::read_to_string(&args[1]).expect("Can't read file");
    let instruction_list: Vec<Instruction> = data.split("\r\n").map(|x|
        Instruction{
            instruction_type: InstructionType::from_str(x.split(" ").collect::<Vec<&str>>()[0]).unwrap(),
            amount: x.split(" ").collect::<Vec<&str>>()[1].parse::<i32>().unwrap_or(0),
        }
    ).collect();
    let mut depth = 0;
    let mut aim = 0;
    for instruction in instruction_list.iter(){
        match instruction.instruction_type {
            InstructionType::Forward => depth += aim * instruction.amount,
            InstructionType::Down => aim += instruction.amount,
            InstructionType::Up => aim -= instruction.amount,
        }
    }
    let sum_forward: i32 = instruction_list.iter().map(|x|
        if matches!(x.instruction_type, InstructionType::Forward) {x.amount} else {0i32}
    ).sum();
    println!("Forward: {}", sum_forward);
    println!("Aim: {}", aim);
    println!("Depth: {}", depth);
    println!("Answer: {}", sum_forward * depth);
}
