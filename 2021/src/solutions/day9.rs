use super::*;

fn low_points(grid: &Array2D<i32>) -> Vec<(usize, usize)>{
    let mut points = Vec::new();
    for col in 0..grid.num_columns(){
        'cell: for row in 0..grid.num_rows(){
            for nb in neighbours(grid, (row, col), false){
                if grid[nb] <= grid[(row, col)] {continue 'cell;}
            }
            points.push((row, col));
        }
    }
    points
}

fn part1(grid: &Array2D<i32>) -> i32{
    low_points(grid).iter().map(|x| grid[*x] + 1).sum()
}

fn part2(grid: &Array2D<i32>) -> i32{
    let mut sizes: Vec<i32> = Vec::new();
    for low_point in low_points(grid){
        let mut set = Vec::new();
        let mut new_values = vec![low_point];
        while !new_values.is_empty() {
            set.extend(new_values.iter());
            new_values = Vec::new();
            for point in &set{
                for nb in neighbours(grid, *point ,false){
                    if grid[nb] != 9 && !set.contains(&nb) &&!new_values.contains(&nb){
                        new_values.push(nb)}
                }
            }
        }
        sizes.push(set.len() as i32);
    }
    let highest_3 = highest_n(3, &sizes);
    highest_3[0] * highest_3[1] * highest_3[2]
}

pub(crate) fn solve(input: &str) -> (String, String){
    let grid = to_grid(input).unwrap_or(Array2D::filled_with(0, 1, 1));
    (part1(&grid).to_string(), part2(&grid).to_string())
}