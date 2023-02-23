use super::*;

struct BingoCard{
    numbers: Vec<u32>,
    hit: [bool; 25],
}

const WINNING_LINES: [[usize;5];10]= [
    // Horizontal lines
    [0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],
    // Vertical lines
    [0,5,10,15,20],[1,6,11,16,21],[2,7,17,22,27],[3,8,13,18,23],[4,9,14,19,24]];

impl BingoCard{
    fn score(&self) -> u32{
        return self.numbers
            .iter()
            .enumerate()
            .map(|(index, &r)| if !self.hit[index] {r} else {0})
            .sum()
    }

    fn hit(&mut self, num: u32) {
        if !self.numbers.contains(&num) {return;}
        let index = self.numbers.iter().position(|x| x == &num).unwrap();
        self.hit[index] = true;
    }

    fn won(&self) -> bool {
        for winning_line in WINNING_LINES{
            if self.hit
                .iter()
                .enumerate()
                .filter(|(index, &_x)| winning_line.contains(index))
                .all(|(_index, &x)| x) {return true;}
        }
        return false;
    }
}

pub(crate) fn solve(input: &str) -> (String, String){
    let blocks = to_blocks(input);
    let blocks_count = blocks.len() - 1;
    let numbers: Vec<u32> = to_nums::<u32>(blocks[0], ",").unwrap_or(Vec::new());
    let mut bingo_cards: Vec<BingoCard> = vec![];
    for block in &blocks.clone()[1..] {
        let nums: Vec<u32> = block
            .split([' ', '\r', '\n'])
            .filter(|x| x != &"")
            .map(|x| x.parse::<u32>().unwrap_or(0))
            .collect();
        bingo_cards.push(BingoCard {
            numbers: nums,
            hit: [false; 25],
        })
    }

    let mut count_solved: usize = 0;
    let mut part1 = 0;
    let mut part2 = 0;

    'outer: for number in numbers {
        for bingo_card in bingo_cards.iter_mut() {
            bingo_card.hit(number);
            if bingo_card.won(){
                if count_solved == 0 {
                    part1 = number * bingo_card.score()
                }
                count_solved += 1;
                if count_solved == blocks_count {
                    part2 = number * bingo_card.score();
                    break 'outer;
                }
            }
        }
        // Remove bingo cards that have won already
        bingo_cards = bingo_cards.into_iter().filter(|x| !x.won()).collect();
    }
    (part1.to_string(), part2.to_string())
}