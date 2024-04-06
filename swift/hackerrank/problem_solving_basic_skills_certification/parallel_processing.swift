import Foundation

/*
 * Complete the 'minTime' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY files
 *  2. INTEGER numCores
 *  3. INTEGER limit
 */

func minTime(files: [Int], numCores: Int, limit: Int) -> Int {
    // Write your code here
    let files = files.sorted()
    var time = 0
    var cores = 0
    var i = 0
    while cores < numCores && i < files.count {
        if files[i] > limit {
            time += files[i] / limit + 1
            cores += 1
        } else {
            time += 1
            cores += 1
        }
        i += 1
    }
    return time
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let filesCount = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

var files = [Int]()

for _ in 1...filesCount {
    guard let filesItem = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
    else { fatalError("Bad input") }

    files.append(filesItem)
}

guard files.count == filesCount else { fatalError("Bad input") }

guard let numCores = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let limit = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

let result = minTime(files: files, numCores: numCores, limit: limit)

fileHandle.write(String(result).data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)
