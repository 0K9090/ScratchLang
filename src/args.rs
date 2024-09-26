use std::path::PathBuf;

type Src = PathBuf;
type Dest = PathBuf;

type SpriteList = Vec<String>;

#[derive(Debug)]
pub enum Task{ Compile(Src, Dest, SpriteList), Decompile(Src, Dest, SpriteList),}

pub fn parse() -> Task{
    let argz_s: String;
    let task: String;
    {
        let mut argz = std::env::args();
        let _ = argz.next();
        task = argz.next().expect("You must use the following syntax: ");
        argz_s = argz.collect::<Vec<String>>().join(" ");
    }
    let path1: Src;
    let path2: Dest;
    {
        let marker1 = argz_s.find(" -t").expect("You must specify destination path with -t <path>.");
        let marker2 = argz_s.find(" -s").unwrap_or_else(||{
            println!("You could specify what sprites to take code from with -s <name_1> <...> <name_n>\n"); argz_s.len()-1usize});
        path1 = PathBuf::from(
            &argz_s[..marker1]
        );
        path2 = PathBuf::from(
            &argz_s[(marker1+4usize)..=marker2]
        );
    }

    if task == "-c" || task == "--compile"{
        return Task::Compile(path1, path2, SpriteList::new());
    } else if task == "-d" || task == "--decompile"{
        return Task::Decompile(path1, path2, SpriteList::new());
    } else {
        panic!("Please specify if you want to compile(-c/--compile) or decompile(-d/--decompile)");
    }
}