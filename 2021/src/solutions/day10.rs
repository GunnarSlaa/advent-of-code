use super::*;

pub(crate) fn solve(input: &str) -> (String, String){
    let lines = to_lines(input);
    let mut score1 = 0;
    let scores = HashMap::from([
        (')', (3, 1)),
        (']', (57, 2)),
        ('}', (1197, 3)),
        ('>', (25137, 4))]);
    let mut score2s: Vec<u64> = Vec::new();
    'outer: for line in lines{
        let mut stack = Vec::new();
        for char in line.chars(){
            if ['(', '[', '{', '<'].contains(&char) { stack.push(char);}
            else{
                let pop = stack.pop().unwrap();
                if opposite_bracket(&pop) != char{
                    score1 += scores[&char].0;
                    continue 'outer;
                }
            }
        }
        stack.reverse();
        let mut linescore = 0;
        for char in stack.iter(){
            linescore *= 5;
            linescore += scores[&opposite_bracket(char)].1;
        }
        score2s.push(linescore);
    }
    score2s.sort();
    (score1.to_string(), score2s[(score2s.len() - 1)/2].to_string())
}