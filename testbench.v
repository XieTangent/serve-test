module testbench;

  // 定义输入和输出端口
  reg clk;
  reg reset;
  reg [7:0] data_in;
  wire [7:0] data_out;

  // 实例化要测试的模块
  // 你需要将下面的 "your_module_name" 替换为你要测试的模块的名称
  your_module dut (
    .clk(clk),
    .reset(reset),
    .data_in(data_in),
    .data_out(data_out)
  );

  // 时钟生成
  always begin
    clk = 0;
    #5 clk = 1;
    #5;
  end

  // 模拟输入数据
  initial begin
    reset = 1;
    data_in = 8'hFF; // 你可以修改这里的数据值来测试不同的情况
    #20 reset = 0;
    #100 $finish;
  end

endmodule
