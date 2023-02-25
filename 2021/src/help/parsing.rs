#![allow(dead_code)]
use std::str::FromStr;
use array2d::Array2D;

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


pub(crate) struct GridBuildError;
pub(crate) fn to_grid(input: &str) -> Result<Array2D<i32>, GridBuildError>{
    let lines = input.split("\r\n").
        map(|x| x.chars()
            .map(|x| x.to_string().parse::<i32>().map_err(|_| GridBuildError))
            .collect::<Result<Vec<i32>, GridBuildError>>())
        .collect::<Result<Vec<Vec<i32>>, GridBuildError>>()?;
    Array2D::from_rows(&lines).map_err(|_| GridBuildError)
}