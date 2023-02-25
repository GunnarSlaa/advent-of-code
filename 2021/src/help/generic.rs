pub(crate) fn highest_n(n: usize, v: &Vec<i32>) -> Vec<i32>{
    let mut highest = v.clone();
    highest.sort();
    highest.reverse();
    highest.truncate(n);
    highest
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
}