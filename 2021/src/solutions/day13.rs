use super::*;

pub(crate) fn solve(input: &str) -> (String, String){
    let blocks = to_blocks(input);
    let dots: Vec<(i32, i32)> = to_lines(blocks[0]).iter()
        .map(|x|to_tuple(x)).collect();
    let mut dots_set:HashSet<(i32,i32)> = HashSet::from_iter(dots.into_iter());
    let instructions = to_lines(blocks[1]);
    let mut answer1: i32 = -1;
    for inst in instructions {
        let instruction = inst
            .split(' ')
            .collect::<Vec<&str>>()
            [2]
            .split('=')
            .collect::<Vec<&str>>();
        let mut new_dots = Vec::new();
        let location = instruction[1].parse::<i32>().unwrap();
        for dot in dots_set.iter() {
            if instruction[0] == "x" && dot.0 > location {
                new_dots.push((location - (dot.0 - location), dot.1));
            } else if instruction[0] == "y" && dot.1 > location {
                new_dots.push((dot.0, location - (dot.1 - location)));
            }
        }
        dots_set.extend(new_dots);
        if instruction[0] == "x" {
            dots_set.retain(|x| x.0 < location);
        } else {
            dots_set.retain(|x| x.1 < location);
        }
        if answer1 == -1 {answer1 = dots_set.len() as i32;}
    }
    (answer1.to_string(), print_grid(dots_set))
}