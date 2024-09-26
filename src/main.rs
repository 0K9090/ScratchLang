
//sb3 from <path> to <path>
//sb3 from <path> to terminal
//... --from-sprite (-s) <sprite-name> IDK IF IT IS POSSIBLE

//use zip::read::ZipArchive;
//mod getjson;
mod args;
#[allow(unused_imports)]
use args::Task;

fn main(){
    let task = args::parse();
    println!("{:#?}", task);
}
