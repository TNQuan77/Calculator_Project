import inc.variable_global

def change_language(language):

	if language == "English":
		
		inc.variable_global.Catalog_select[0][0] = "Scientific Constant"
		inc.variable_global.Catalog_select[0][1][0][0] = "Math"
		inc.variable_global.Catalog_select[0][1][1][0] = "Universal"
		inc.variable_global.Catalog_select[0][1][2][0] = "Electromagnetic"
		inc.variable_global.Catalog_select[0][1][3][0] = "Atomic & Nuclear"
		inc.variable_global.Catalog_select[0][1][4][0] = "Physico - Chem"
		inc.variable_global.Catalog_select[0][1][5][0] = "Adopted Values"
		inc.variable_global.Catalog_select[0][1][6][0] = "Other"
		inc.variable_global.Catalog_select[1][0] = "Unit Conversions"
		inc.variable_global.Catalog_select[1][1][0][0] = "Length"
		inc.variable_global.Catalog_select[1][1][1][0] = "Area"
		inc.variable_global.Catalog_select[1][1][2][0] = "Volume"
		inc.variable_global.Catalog_select[1][1][3][0] = "Mass"
		inc.variable_global.Catalog_select[1][1][4][0] = "Velocity"
		inc.variable_global.Catalog_select[1][1][5][0] = "Pressure"
		inc.variable_global.Catalog_select[1][1][6][0] = "Energy"
		inc.variable_global.Catalog_select[1][1][7][0] = "Power"
		inc.variable_global.Catalog_select[1][1][8][0] = "Temperature"
		inc.variable_global.Catalog_select[2][0] = "Probability"
		inc.variable_global.Catalog_select[3][0] = "Numerical Calculation"
		inc.variable_global.Catalog_select[4][0] = "Hyperbolic/Trigonometric"

	elif language == "Vietnamese":
		
		inc.variable_global.Catalog_select[0][0] = "Hằng số khoa học"
		inc.variable_global.Catalog_select[0][1][0][0] = "Hằng số toán học"
		inc.variable_global.Catalog_select[0][1][1][0] = "Hằng số chung"
		inc.variable_global.Catalog_select[0][1][2][0] = "Hằng số điện từ"
		inc.variable_global.Catalog_select[0][1][3][0] = "Hằng số nguyên tử & Hạt nhân"
		inc.variable_global.Catalog_select[0][1][4][0] = "Hằng số Lý - Hóa"
		inc.variable_global.Catalog_select[0][1][5][0] = "Giá trị thông qua"
		inc.variable_global.Catalog_select[0][1][6][0] = "Khác"
		inc.variable_global.Catalog_select[1][0] = "Chuyển đổi đơn vị"
		inc.variable_global.Catalog_select[1][1][0][0] = "Độ dài"
		inc.variable_global.Catalog_select[1][1][1] [0] = "Diện tích"
		inc.variable_global.Catalog_select[1][1][2][0] = "Thể tích"
		inc.variable_global.Catalog_select[1][1][3] [0] = "Khối lượng"
		inc.variable_global.Catalog_select[1][1][4] [0] = "Vận tốc"
		inc.variable_global.Catalog_select[1][1][5][0] = "Áp suất"
		inc.variable_global.Catalog_select[1][1][6][0] = "Năng lượng"
		inc.variable_global.Catalog_select[1][1][7][0] = "Công suất"
		inc.variable_global.Catalog_select[1][1][8] [0] = "Nhiệt độ"
		inc.variable_global.Catalog_select[2][0] = "Xác suất"
		inc.variable_global.Catalog_select[3][0] = "Phép tính số"
		inc.variable_global.Catalog_select[4][0] = "Hyperbol/Lượng giác"
	
	elif language == "Chinese":
		
		inc.variable_global.Catalog_select[0][0] = "科学常数"
		inc.variable_global.Catalog_select[0][1][0][0] = "数学常数"
		inc.variable_global.Catalog_select[0][1][1][0] = "通用常量"
		inc.variable_global.Catalog_select[0][1][2][0] = "电磁常数"
		inc.variable_global.Catalog_select[0][1][3][0] = "原子和核常数"
		inc.variable_global.Catalog_select[0][1][4][0] = "物理 - 化学常数"
		inc.variable_global.Catalog_select[0][1][5][0] = "传递的值"
		inc.variable_global.Catalog_select[0][1][6][0] = "其他"
		inc.variable_global.Catalog_select[1][0] = "单位换算"
		inc.variable_global.Catalog_select[1][1][0][0] = "长度"
		inc.variable_global.Catalog_select[1][1][1] [0] = "区域"
		inc.variable_global.Catalog_select[1][1][2][0] = "体积"
		inc.variable_global.Catalog_select[1][1][3] [0] = "音量"
		inc.variable_global.Catalog_select[1][1][4] [0] = "速度"
		inc.variable_global.Catalog_select[1][1][5][0] = "压力"
		inc.variable_global.Catalog_select[1][1][6][0] = "能源"
		inc.variable_global.Catalog_select[1][1][7][0] = "容量"
		inc.variable_global.Catalog_select[1][1][8] [0] = "温度"
		inc.variable_global.Catalog_select[2][0] = "概率"
		inc.variable_global.Catalog_select[3][0] = "数值计算"
		inc.variable_global.Catalog_select[4][0] = "双曲/三角"
	
	
	elif language == "Japanese":
		
		inc.variable_global.Catalog_select[0][0] = "科学定数"
		inc.variable_global.Catalog_select[0][1][0][0] = "数学定数"
		inc.variable_global.Catalog_select[0][1][1][0] = "一般定数"
		inc.variable_global.Catalog_select[0][1][2][0] = "電磁定数"
		inc.variable_global.Catalog_select[0][1][3][0] = "原子および核定数"
		inc.variable_global.Catalog_select[0][1][4][0] = "物理定数 - 化学定数"
		inc.variable_global.Catalog_select[0][1][5][0] = "渡された値"
		inc.variable_global.Catalog_select[0][1][6][0] = "その他"
		inc.variable_global.Catalog_select[1][0] = "単位換算"
		inc.variable_global.Catalog_select[1][1][0][0] = "長さ"
		inc.variable_global.Catalog_select[1][1][1] [0] = "エリア"
		inc.variable_global.Catalog_select[1][1][2][0] = "ボリューム"
		inc.variable_global.Catalog_select[1][1][3] [0] = "ボリューム"
		inc.variable_global.Catalog_select[1][1][4] [0] = "速度"
		inc.variable_global.Catalog_select[1][1][5][0] = "圧力"
		inc.variable_global.Catalog_select[1][1][6][0] = "エネルギー"
		inc.variable_global.Catalog_select[1][1][7][0] = "容量"
		inc.variable_global.Catalog_select[1][1][8] [0] = "温度"
		inc.variable_global.Catalog_select[2][0] = "確率"
		inc.variable_global.Catalog_select[3][0] = "数値計算"
		inc.variable_global.Catalog_select[4][0] = "双曲線/三角関数"