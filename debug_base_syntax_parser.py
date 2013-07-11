from src import BaseSyntaxSerializer, BaseSyntaxParser


parser = BaseSyntaxParser('expression', debug=True)


print('\n\nNotice: After typing a query - enter two minuses on a new line')

while True:
    print('\n')

    try:
        lines = []
        while True:
            new_line = input('> ')
            if new_line == '--':
                break
            lines.append(new_line)

        node = parser.parse('\n'.join(lines), debug=True)
        string = BaseSyntaxSerializer(node).output

        print('\n Parsed result: \n')
        print(string)
    except:
        pass

    print('\n')

    cmd = input('Press any key and enter to exit or just enter to repeat...')

    if cmd:
        break
