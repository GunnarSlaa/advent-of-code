use array2d::Array2D;

pub(crate) fn neighbours(grid: &Array2D<i32>, (row, col): (usize, usize), diagonal: bool) -> Vec<(usize, usize)>{
    neighbours_from_size(&(grid.num_rows(), grid.num_columns()), (row, col), diagonal)
}

pub(crate) fn neighbours_from_size((rows, cols): &(usize, usize), (row, col): (usize, usize), diagonal: bool) -> Vec<(usize, usize)>{
    let mut neighbours = Vec::new();
    if row > 0 {neighbours.push((row - 1, col))}
    if col > 0 {neighbours.push((row, col - 1))}
    if col < (cols - 1)  {neighbours.push((row, col + 1))}
    if row < (rows - 1)  {neighbours.push((row + 1, col))}
    if diagonal{
        if row > 0 && col > 0 {neighbours.push((row - 1, col - 1))}
        if row > 0 && col < (cols - 1) {neighbours.push((row - 1, col + 1))}
        if row < (rows - 1) && col > 0 {neighbours.push((row + 1, col - 1))}
        if row < (rows - 1) && col < (cols - 1) {neighbours.push((row + 1, col + 1))}
    }
    neighbours
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_neighbours() {
        let grid = Array2D::filled_with(0, 3, 3);
        assert_eq!(neighbours(&grid, (0, 0), false).len(), 2);
        assert_eq!(neighbours(&grid, (1, 1), false).len(), 4);
        assert_eq!(neighbours(&grid, (2, 1), false).len(), 3);
        assert_eq!(neighbours(&grid, (0, 0), true).len(), 3);
        assert_eq!(neighbours(&grid, (1, 1), true).len(), 8);
        let grid2 = Array2D::filled_with(0, 5, 3);
        assert_eq!(neighbours(&grid2, (0, 0), false).len(), 2);
        assert_eq!(neighbours(&grid2, (4, 2), false).len(), 2);
        assert_eq!(neighbours(&grid2, (4, 2), false), vec![(3, 2), (4, 1)]);
        assert_eq!(neighbours(&grid2, (4, 1), false).len(), 3);
        assert_eq!(neighbours(&grid2, (4, 1), true).len(), 5);
    }
}