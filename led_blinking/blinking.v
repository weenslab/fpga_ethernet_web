module blinking
    (
        input wire clk,
        input wire rst_n,
        output reg led
    );
    
    reg [25:0] cnt_reg; // Max count = 2^26 = 67108864
    
    always @(posedge clk)
    begin
        if (!rst_n)
        begin
            cnt_reg <= 0;
            led <= 0;
        end
        else
        begin
            if (cnt_reg >= 26'd50000000) // 1 second in 50 MHz clock
            begin
                cnt_reg <= 0;
                led <= ~led;
            end
            else
            begin
                cnt_reg <= cnt_reg + 1;
            end
        end
    end
    
endmodule
