use super::*;

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

pub(crate) fn solve(input: &str) -> (String, String){
    let instruction_list: Vec<Instruction> = input.split("\r\n")
        .map(|x|{
            let instruction_string = x.split(" ").collect::<Vec<&str>>();
            Instruction {
                instruction_type: InstructionType::from_str(instruction_string[0]).unwrap(),
                amount: instruction_string[1].parse::<i32>().unwrap_or(0),
            }
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
    let sum_down: i32 = instruction_list.iter().map(|x|
        if matches!(x.instruction_type, InstructionType::Down) {x.amount} else {0i32}
    ).sum();
    let sum_up: i32 = instruction_list.iter().map(|x|
        if matches!(x.instruction_type, InstructionType::Up) {x.amount} else {0i32}
    ).sum();
    ((sum_forward * (sum_down - sum_up)).to_string(),(sum_forward * depth).to_string())
}