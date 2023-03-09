use super::*;

fn count_chars(s: String, letters: &[char]) -> Vec<u64>{
    let mut char_counts: HashMap<char, u64> = HashMap::new();
    for l in letters.iter() {
        char_counts.insert(*l, s.matches(*l).count() as u64);
    }
    let mut keys: Vec<&char> = char_counts.keys().collect();
    keys.sort();
    keys.into_iter().map(|x| char_counts[x]).collect()
}

fn run_n_times(mut string: String, rules: &HashMap<&str, char>, n: i32) -> String{
    for _ in 0..n{
        let mut new_string = string.clone();
        for i in 0..(string.len() - 1){
            new_string.insert(2 * i + 1, rules[&string[i..i + 2]])
        }
        string = new_string;
    }
    string
}

fn sum_vec(mut a: Vec<u64>, b: &[u64]) -> Vec<u64>{
    if a.len() < b.len() {
        a.resize(b.len(), 0);
    }

    for (ai, bi) in a.iter_mut().zip(b) {
        *ai += *bi;
    }
    a
}

fn part1(mut polymer: String, rules: &HashMap<&str, char>, letters: &[char]) -> u64{
    polymer = run_n_times(polymer, rules, 10);
    let char_count = count_chars(polymer, letters);
    let most = char_count.iter().max().unwrap();
    let least = char_count.iter().min().unwrap();
    println!("1: {most}, {least}");
    most - least
}

fn part2(polymer: String, rules: &HashMap<&str, char>, letters: &[char]) -> u64{
    let mut after_10strings = HashMap::new();
    let mut after_10scores = HashMap::new();
    for combo in rules.keys() {
        let mut string = combo.to_string();
        string = run_n_times(string, rules, 10);
        after_10strings.insert(combo.to_string(), string.clone());
        after_10scores.insert(combo.to_string(), count_chars(string[1..].to_string(), letters));
    }
    let mut after_20scores = HashMap::new();
    for combo in rules.keys() {
        let string = after_10strings[*combo].to_string();
        let mut score = Vec::new();
        score = sum_vec(score, &count_chars(string[0..0].to_string(), letters));
        for i in 0..(string.len() - 1){
            score = sum_vec(score, &after_10scores[&string[i..i + 2]])
        }
        after_20scores.insert(combo.to_string(), score);
    }
    let mut after_30scores = HashMap::new();
    for combo in rules.keys() {
        let string = after_10strings[*combo].to_string();
        let mut score = Vec::new();
        score = sum_vec(score, &count_chars(string[0..0].to_string(), letters));
        for i in 0..(string.len() - 1){
            score = sum_vec(score, &after_20scores[&string[i..i + 2]])
        }
        after_30scores.insert(combo.to_string(), score);
    }
    let mut after_40scores = HashMap::new();
    for combo in rules.keys() {
        let string = after_10strings[*combo].to_string();
        let mut score = Vec::new();
        score = sum_vec(score, &count_chars(string[0..0].to_string(), letters));
        for i in 0..(string.len() - 1){
            score = sum_vec(score, &after_30scores[&string[i..i + 2]])
        }
        after_40scores.insert(combo.to_string(), score);
    }
    let mut score = Vec::new();
    score = sum_vec(score, &count_chars(polymer[0..0].to_string(), letters));
    for i in 0..(polymer.len() - 1){
        score = sum_vec(score, &after_40scores[&polymer[i..i + 2]])
    }
    let most = score.iter().max().unwrap();
    let least = score.iter().min().unwrap();
    println!("2: {most}, {least}");
    most - least
}

pub(crate) fn solve(input: &str) -> (String, String){
    let blocks = to_blocks(input);
    let polymer = blocks[0].to_string();
    let mut rules = HashMap::new();
    for i in to_lines(blocks[1]).iter(){
        let splits: Vec<&str> = i.split(' ').collect();
        rules.insert(splits[0], splits[2].chars().next().unwrap());
    }
    let mut letters_set = HashSet::new();
    for key in rules.keys(){
        for c in key.chars(){
            letters_set.insert(c);
        }
    }
    let letters = Vec::from_iter(letters_set);
    (part1(polymer.clone(), &rules, &letters).to_string(), part2(polymer, &rules, &letters).to_string())
}