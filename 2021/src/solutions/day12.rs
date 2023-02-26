use super::*;

fn can_visit(path: &[&str], next: &str, part: i32) -> bool{
    if part == 1{
        is_upper(next) || !path.contains(&next)
    }
    else{
        if is_upper(next) {return true;}
        if next == "start" {return false;}
        if !path.contains(&next) {return true;}
        let mut found_lowers = Vec::new();
        for node in path{
            if is_lower(node){
                if found_lowers.contains(node) {return false;}
                else {found_lowers.push(node)}
            }
        }
        true
    }
}

fn solve_part(connections: &HashMap<&str, Vec<&str>>, part: i32) -> i32{
    let mut paths = vec![vec!["start"]];
    let mut complete_paths = Vec::new();
    loop{
        let mut new_paths = Vec::new();
        for path in paths{
            for next in connections[path[path.len() - 1]].iter(){
                if next == &"end" {
                    let mut new_path = path.clone();
                    new_path.push("end");
                    complete_paths.push(new_path);
                }
                else if can_visit(&path, next, part){
                    let mut new_path = path.clone();
                    new_path.push(next);
                    new_paths.push(new_path);
                }
            }
        }
        paths = new_paths;
        if paths.is_empty(){break;}
    }
    complete_paths.len() as i32
}

pub(crate) fn solve(input: &str) -> (String, String) {
    let lines = to_lines(input);
    let mut connections: HashMap<&str, Vec<&str>> = HashMap::new();
    for line in lines{
        let caves: Vec<&str> = line.split('-').collect();
        connections.entry(caves[0])
            .or_insert_with(Vec::new)
            .push(caves[1]);
        connections.entry(caves[1])
            .or_insert_with(Vec::new)
            .push(caves[0]);
    }
    (solve_part(&connections, 1).to_string(), solve_part(&connections, 2).to_string())
}