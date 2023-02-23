#[allow(dead_code)]
use std::str::FromStr;

pub(crate) fn to_lines (input: &str) -> Vec<&str>{
    input.split("\r\n").collect()
}

pub(crate) struct ToNumsError;

pub(crate) fn to_nums<F: FromStr>(input: &str, pattern: &str) -> Result<Vec<F>, ToNumsError>{
    input.split(pattern)
        .map(|x| x.parse::<F>().map_err(|_| ToNumsError))
        .collect::<Result<Vec<F>, ToNumsError>>()
}

pub(crate) fn to_blocks (input: &str) -> Vec<&str>{
    input.split("\r\n\r\n").collect()
}