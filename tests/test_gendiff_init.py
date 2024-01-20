from gendiff.__init__ import generate_diff


def test_generate_diff():
    file_path1 = './tests/fixtures/file1.json'
    file_path2 = './tests/fixtures/file2.json'
    result = generate_diff(file_path1, file_path2)
    correct = open('./tests/fixtures/result_json.txt')
    assert result == correct.read()
