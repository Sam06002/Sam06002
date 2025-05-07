import os

def generate_snake():
    svg_content = '''
    <svg width="100%" height="100%" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 10 l20 0 l0 20 l20 0 l0 20 l20 0 l0 20"
              stroke="rgb(0,0,0)" stroke-width="2" fill="none"/>
    </svg>
    '''
    
    os.makedirs('output', exist_ok=True)
    with open('output/snake.svg', 'w') as f:
        f.write(svg_content)

if __name__ == "__main__":
    generate_snake()
