use std::collections::HashSet;

pub(crate) fn highest_n(n: usize, v: &Vec<i32>) -> Vec<i32>{
    let mut highest = v.clone();
    highest.sort();
    highest.reverse();
    highest.truncate(n);
    highest
}

pub(crate) fn opposite_bracket(c: &char) -> char{
    match c{
        '(' => ')',
        '[' => ']',
        '{' => '}',
        '<' => '>',
        ')' => '(',
        ']' => '[',
        '}' => '{',
        '>' => '<',
        _ => 'X'
    }
}

pub(crate) fn is_upper(s: &str) -> bool{
    s.chars().all(char::is_uppercase)
}

pub(crate) fn is_lower(s: &str) -> bool{
    s.chars().all(char::is_lowercase)
}

pub(crate) fn to_tuple(s: &str) -> (i32, i32){
    let mut split = s.split(',');
    (split.next().unwrap().parse::<i32>().unwrap(),
     split.next().unwrap().parse::<i32>().unwrap())
}

pub(crate) fn print_grid(dots: HashSet<(i32, i32)>) -> String{
    let max_x = dots.clone().into_iter().map(|(v,_)|v).fold(0, std::cmp::max);
    let max_y = dots.clone().into_iter().map(|(_,v)|v).fold(0, std::cmp::max);
    let mut output = "".to_string();
    for row in 0..(max_y + 1){
        output.push('\n');
        for col in 0..(max_x + 1){
            output.push_str(if dots.contains(&(col, row)) {"##"} else {"  "});
        }
    }
    output
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_highest_n() {
        assert_eq!(highest_n(1, &vec![1, 3, 5]), vec![5]);
        assert_eq!(highest_n(2, &vec![0, 1, 2, 3, 4]), vec![4, 3]);
        assert_eq!(highest_n(3, &vec![9, 3, 87, 4, 2]), vec![87, 9, 4]);
        assert_eq!(highest_n(4, &vec![1, 3, 5]), vec![5, 3, 1]);
    }

    #[test]
    fn test_opposite_bracket(){
        assert_eq!(opposite_bracket(&'<'), '>');
        assert_eq!(opposite_bracket(&'}'), '{');
    }

    #[test]
    fn test_is_upper(){
        assert!(is_upper("HALLO"));
        assert!(!is_upper("HALlO"));
        assert!(!is_upper("HALLO3"));
    }

    #[test]
    fn test_is_lower(){
        assert!(is_lower("hallo"));
        assert!(!is_lower("halLo"));
        assert!(!is_lower("hallo3"));
    }
}