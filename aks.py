import requests

verilog_code = """
module full_adder(input A, input B, input Cin, output S, output Cout);
    assign S = A ^ B ^ Cin;
    assign Cout = (A & B) | (B & Cin) | (A & Cin);
endmodule
"""

url = 'https://da8f-61-216-173-4.ngrok-free.app/compile'
response = requests.post(url, json={'verilog_code': verilog_code})
print(response.json())
