from exp_sin import evaluate_expression

def process_expressions(input_file, output_file):
    """Processa as expressões matemáticas de um input.txt e escreve os resultados em output.txt."""
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if line:
                try:
                    result = evaluate_expression(line)

                    formatted_result = f"{result:.1f}"
                    f_out.write(f"{formatted_result}\n")
                except Exception as e:
                    f_out.write(f"Error: {e}\n")

def main():
    input_file = "input.txt"
    output_file = "output.txt"
    try:
        process_expressions(input_file, output_file)
        print(f"Resultados escritos em '{output_file}'.")
    except FileNotFoundError:
        print(f"Erro: '{input_file}' não encontrado.")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()