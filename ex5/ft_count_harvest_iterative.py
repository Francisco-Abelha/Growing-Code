# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fgoncal2 <fgoncal2@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/08 16:02:22 by fgoncal2          #+#    #+#              #
#    Updated: 2026/01/08 16:23:24 by fgoncal2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	i = 1
	while (i <= days):
		print("Day", i)
		i += 1
	print("Harvest time!")
	