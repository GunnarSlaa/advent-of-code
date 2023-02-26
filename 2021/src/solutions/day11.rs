use super::*;

pub(crate) fn solve(input: &str) -> (String, String){
    let mut grid = to_grid(input).unwrap_or(Array2D::filled_with(0, 1, 1));
    let mut flashes = 0;
    let mut answer1 = 0;
    let mut answer2 = 0;
    'outer: for i in 0..1000{
        let mut flashed = Vec::new();
        for col in 0..10{
            for row in 0..10{
                grid[(row,col)] += 1;
            }
        }
        let mut to_flash;
        loop {
            to_flash = Vec::new();
            for col in 0..10{
                for row in 0..10{
                    if grid[(row,col)] > 9 && !flashed.contains(&(row, col)) {to_flash.push((row,col))}
                }
            }
            if to_flash.is_empty() {break;}
            for cell in to_flash{
                for nb in neighbours(&grid, cell, true){
                    grid[nb] += 1;
                }
                flashed.push(cell);
                flashes += 1;
            }
        }
        if flashed.len() == 100 {answer2 = i + 1; break 'outer;}
        if i == 99 {answer1 = flashes;}
        for cell in flashed{grid[cell] = 0;}
    }
    (answer1.to_string(), answer2.to_string())
}