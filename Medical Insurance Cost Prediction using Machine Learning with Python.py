{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f499e3da-70b0-4a9b-8956-c03c508b10d1",
   "metadata": {},
   "source": [
    "Importing the Dependencies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "737c6089-67f5-4e29-aab5-79f70874e61e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn import metrics"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d437e88-4a3d-44bc-8ab4-e5b860c9c35d",
   "metadata": {},
   "source": [
    "Data Collection and Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9159f188-28a6-46f6-831c-6b22764aaed6",
   "metadata": {},
   "outputs": [],
   "source": [
    "Insurance_Data = pd.read_csv(r'C:\\Users\\Dell\\Downloads\\insurance.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a4155028-1e86-43af-a345-dd1558b33aba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.900</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.770</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.000</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.705</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.880</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.85520</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age     sex     bmi  children smoker     region      charges\n",
       "0   19  female  27.900         0    yes  southwest  16884.92400\n",
       "1   18    male  33.770         1     no  southeast   1725.55230\n",
       "2   28    male  33.000         3     no  southeast   4449.46200\n",
       "3   33    male  22.705         0     no  northwest  21984.47061\n",
       "4   32    male  28.880         0     no  northwest   3866.85520"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Inspecting the first few rows of the dataset\n",
    "Insurance_Data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0c9f0cc5-f2c7-4515-bfb0-1ea6f1ddbaaf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1338, 7)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Insurance_Data.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5effe569-9dd7-4802-9224-23218af746da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1338 entries, 0 to 1337\n",
      "Data columns (total 7 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   age       1338 non-null   int64  \n",
      " 1   sex       1338 non-null   object \n",
      " 2   bmi       1338 non-null   float64\n",
      " 3   children  1338 non-null   int64  \n",
      " 4   smoker    1338 non-null   object \n",
      " 5   region    1338 non-null   object \n",
      " 6   charges   1338 non-null   float64\n",
      "dtypes: float64(2), int64(2), object(3)\n",
      "memory usage: 73.3+ KB\n"
     ]
    }
   ],
   "source": [
    "# Displaying the dataset information (data types, non-null counts)\n",
    "Insurance_Data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c31a1ef-1e1c-46fd-adb4-52a975cd8e25",
   "metadata": {},
   "source": [
    "Categorical Features:\n",
    "- Sex\n",
    "- Smoker\n",
    "- Region"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f6e5e829-38ea-4421-a932-7846a933f7e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age         0\n",
       "sex         0\n",
       "bmi         0\n",
       "children    0\n",
       "smoker      0\n",
       "region      0\n",
       "charges     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# checking for missing values\n",
    "Insurance_Data.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6f4fe0f-e0e4-495f-868c-78c2febce12e",
   "metadata": {},
   "source": [
    "Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f8f831c2-7a8f-4066-9356-dfcbde5b425c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>39.207025</td>\n",
       "      <td>30.663397</td>\n",
       "      <td>1.094918</td>\n",
       "      <td>13270.422265</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.049960</td>\n",
       "      <td>6.098187</td>\n",
       "      <td>1.205493</td>\n",
       "      <td>12110.011237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>15.960000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1121.873900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>27.000000</td>\n",
       "      <td>26.296250</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4740.287150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>30.400000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>9382.033000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>34.693750</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>16639.912515</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.000000</td>\n",
       "      <td>53.130000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>63770.428010</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               age          bmi     children       charges\n",
       "count  1338.000000  1338.000000  1338.000000   1338.000000\n",
       "mean     39.207025    30.663397     1.094918  13270.422265\n",
       "std      14.049960     6.098187     1.205493  12110.011237\n",
       "min      18.000000    15.960000     0.000000   1121.873900\n",
       "25%      27.000000    26.296250     0.000000   4740.287150\n",
       "50%      39.000000    30.400000     1.000000   9382.033000\n",
       "75%      51.000000    34.693750     2.000000  16639.912515\n",
       "max      64.000000    53.130000     5.000000  63770.428010"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Insurance_Data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fdd7cbee-6a35-438d-888d-0dcf158e8058",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_7868\\3168055361.py:4: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(Insurance_Data['age'])\n"
     ]
    },
    {
     "data": {
      "image/png": "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Yv/+/di5cycWL16MSZMmISYmBgqFAjNmzMDatWvxxRdfIC8vD2+88QY2b96M2bNnAwDGjBkDURTx+OOP49ixYzhw4ABmz56N8PBw3HLLLVI+HURERHQZknYPAY7F4qxWK5566imYTCakp6dj9erVUKvVKCwsxNixY7Fs2TJMnjwZgiBg5cqVWLJkCaZPnw6NRoPx48fjySefdO5v5syZ0Gg0ePnll1FUVIQePXrglVdewdixYwE4uqTefvttLF++HFOmTIEoihgxYgTeeeedRuNqiIiIyLsIoi904nsBm82Oyso6SeugUikQFhaIqqo62fdpCoKAWlM99h0vd3kgrlIhICBAA4PB3KIxLWo/JVJ7RiJI6yfrMS2+9Pq7g+1n+9l+ebY/PDzQ5YG4vj2hm4iIiHwGQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREckCQwsRERHJAkMLERERyQJDCxEREcmC5KHFbrcjMzMTI0eORGpqKmbMmIH8/PxLlq+qqsJjjz2G9PR0pKenY9GiRTAYDM77bTYbMjMzMWbMGAwYMACTJ0/Gt99+26J9EBERkfeRPLSsWrUK69atw9KlS7F+/XoIgoCZM2fCYrE0W37OnDkoKCjA2rVrkZmZie3bt2PJkiXO+1esWIF169ZhyZIl+OKLLzBu3Dj85S9/wYEDB1zeBxEREXkfSUOLxWLBmjVrMHv2bIwePRpJSUlYsWIFSkpKsHXr1ibl9+7di+zsbCxbtgzJyckYPnw4nnnmGWzatAklJSUAAKvVioULF2LUqFHo0qULHnzwQQQGBiIrK8vlfRAREZH3kTS05Obmoq6uDsOGDXNu0+l06NevH3JycpqU37VrF6KiopCY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N998s5iTkyOeOHFC/Pvf/y4OGDBAPH78eIdo/+233y7ecccd4v79+8Xjx4+Ls2fPFkeMGCEaDIYO0f4GFotFnDx5sti7d2/xk08+EUWxY7z/v/nmGzElJUUsKSkRS0tLnTej0dgh2r9x40axb9++4tq1a8W8vDxx5cqVYlJSkrhnz54O0X6z2dzodS8tLRV//vlnsV+/fuKHH37o888BQ4sMFRcXi/fdd584cOBAcfz48Y1Cy+uvvy6OHDlSrK+vd2578cUXxRtuuEGKqnpcXl6e2Lt3b3H37t3ObXa7XRw3bpz4z3/+0+fbX1lZKc6dO1c8evSoc9vhw4fF3r17i/v27fP59l/oxRdfFP/85z83Ci0dof2vvfaaePPNNzd7n6+33263i2PGjBGfe+65RttnzJghvv766z7f/uZYLBZx4sSJ4iOPPCKKou+/B9g9JEMHDx5ESEgIPvvsM6Smpja6b9euXUhPT4dKpXJuGzZsGE6dOoWKior2rqrHhYWF4Y033kD//v2d2wRBgCiKqKmp6RDtf+mll9CrVy8AQHl5OVavXo3Y2Fj07NnT59vfICcnB+vXr8fzzz/faHtHaP+RI0fQs2fPZu/z9fafPHkSZ86cwU033dRo++rVq/HAAw/4fPub895776GoqAhPPvkkAN9/DzC0yNC1116LF198EV26dGlyX3FxMWJjYxtti46OBgCcPXu2XerXlnQ6HUaPHg21Wu3c9uWXX+L06dO4+uqrfb79F1q0aBFGjBiB//73v/i///s/BAQEdIj26/V6PP7443jqqacQFxfX6L6O0P6jR4+ioqICU6dOxVVXXYUpU6bgp59+AuD77c/LywMAGAwG3HfffRg+fDhuv/12fPvttwB8v/0XM5vNeP311zF9+nRnO339OWBo8TEmk6nRFzoA59WrzWazFFVqU7t378Zf//pXjB07Ftdee22Hav/06dPxySef4Oabb8bDDz+MgwcPdoj2P/300xg4cGCTX9uA77//LRYL8vLyUFtbi0ceeQRvvPEGUlJSMHPmTOzYscPn219bWwsAeOKJJ3DjjTdizZo1GDFiBB566KEO0f6Lbdq0CWazudFkDF9/DlRXLkJyotVqYbFYGm1reKMGBARIUaU2s23bNsybNw+pqal46aWXAHSs9jd0Efz973/Hr7/+iv/85z8+3/6NGzdi165d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",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'age' column\n",
    "sns.set()\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.distplot(Insurance_Data['age'])\n",
    "plt.title('Age Distribution')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ffe4ebf6-1031-4ed9-9fb8-dc4d27961a15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiAAAAImCAYAAABq0DEBAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA7ZElEQVR4nO3deVyVdd7/8ffhEJuICy4wDqbhgqigJiNajOZEjZkzIXlbiamoaTKaG5ZpLiWaibkOWYDLjBZkOFa23S63TSWD2uYkkmlGliKKJi4sweH3hz/P3Nyo0VG/B/H1fDx83HIt53wu4/J+zXVdHC0VFRUVAgAAMMjF2QMAAICbDwECAACMI0AAAIBxBAgAADCOAAEAAMYRIAAAwDgCBAAAGEeAAAAA4wgQADckZ3+GorPfH7jRESBALbN//35NmDBBd9xxhzp06KA777xT48ePV3Z2tpH337Bhg9q2bVvpV8eOHdW7d28988wzOnbsWKXtly1bprZt21b79fPy8jRq1Cj9+OOPV9wuKytLbdu2VVZWlkPvcyVbt27Vk08+edn3AvDLXJ09AIBr55tvvtHAgQMVEhKiadOmqVGjRsrLy9PatWs1cOBA/f3vf1enTp2MzLJ8+XI1btxYklRUVKRvvvlGL7/8srZt26a0tDQFBARIkgYMGKCIiIhqv+6OHTu0fft2PfPMM1fcrn379kpPT1erVq0cP4jLWL16tbH3AmorAgSoRVatWqX69esrJSVFt9xyi3353XffrT59+igpKUmvvPKKkVnatWun3/72t/avu3fvrrvuukv9+/fXjBkztGrVKkmSn5+f/Pz8rvn7e3t7G4stk+8F1BbcggFqkRMnTkiq+nyCl5eXpk6dqj59+lRavmXLFvXv318dO3bUHXfcoTlz5uj8+fOSpLNnz6p379764x//qNLSUvvrxsbGqnv37vb3+jUCAgL0X//1X9qxY4e+//57SVVvjRw+fFiPP/64unXrptDQUA0cOFAffvihpAu3d6ZOnSpJ+sMf/qCnnnpKktS7d2/NnTtXQ4YMUZcuXTRjxozL3hbZsmWL7r33XnXs2FEDBgxQZmamfd3l9hk8eLAGDx5s//3OnTu1c+dO+7aX2u/f//63hg8frm7duqlLly4aPXq0vvnmmyrvlZmZqdjYWIWGhqpHjx6aP3++ysrKfvWfLXCjIUCAWqRXr146cuSIHnroIa1bt04HDx60x8gf//hHRUVF2bd9++23FRcXp9tuu01//etf9Ze//EVvvfWWxowZo4qKCnl7eyshIUHfffedVqxYIUl69dVX9cknnyghIUGNGjVyaMY777xTkvTpp59WWWez2TRq1CidP39eL7zwgpKSklS/fn2NGTNGubm56tWrlx5//HFJF27xjBkzxr7vunXr1LZtWy1btkx//vOfL/v+Tz/9tB599FEtW7ZMderU0ciRI3XgwIFqzz9z5kwFBwcrODhY6enpat++fZVt/vWvf+nhhx+WzWZTQkKC5syZo6NHj+qhhx7SwYMHK207efJk3X777VqxYoX69eunlStX6o033qj2PMCNilswQC3yyCOP6Pjx40pNTdWzzz4rSWrQoIHuvPNODR48WKGhoZIuXMlITExURESEEhMT7fu3aNFCQ4cO1YcffqhevXqpe/fueuSRR/TKK6+oU6dOSkxM1MCBA9W7d2+HZ7z4XMjx48errCsoKNDBgwc1evRo9ezZU5IUEhKi5cuXq6SkRLfeequaN28uqeotniZNmuipp56Si8uF/111uQdCZ86cqb59+0q6cFvoD3/4g1566SUtXLiwWvO3atVK3t7eknTZ2y4LFy5UQECAUlJSZLVaJV0Ir8jISC1btkyLFy+2bztgwADFxcXZ59myZYu2b9+uhx56qFrzADcqroAAtcwTTzyhjz76SAsXLtSDDz4ob29vvf322xo4cKDWrFkjSfr222+Vl5en3r17q6yszP4rLCxM3t7e+uSTT+yvN3nyZPn7+2vUqFFq0qSJ/RbI1bJYLFWWNWrUSK1atdIzzzyjp556Su+++64qKio0depUtWnT5oqvFxgYaI+Py7FarbrnnnvsX7u7u+v3v/+9duzY4dhBXML58+f173//W/fdd589PiTJx8dHd911V5Uw6ty5c6Wv/fz87LfBgNqMAAFqoXr16un+++9XQkKCtmzZon/84x9q1aqVEhMTderUKf3000+SpNmzZ6t9+/aVfp09e1b5+fn21/Ly8tK9994rm82m8PBweXp6XtVsF38M91IPnlosFq1cuVJRUVH66KOPNGHCBPXo0UPjx4+3z3w51bklVL9+/UoP50qSr6+vCgsLq38Av+DMmTOqqKi45DyNGjXSmTNnKi3z8PCo9LWLiwufMYKbArdg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2efnjfm3w//i4eEhSVUeOC0pKZGnp6czRgIAAL/ghg+Qi7de8vPzKy3Pz8+Xn5+fM0YCAAC/4IYPkKCgIHl7eysrK8u+rLCwUNnZ2eratasTJwMAAJdzwz8D4ubmppiYGCUmJqphw4Zq1qyZFixYID8/P0VGRjp7PAAAcAk3fIBI0rhx41RWVqbp06eruLhYYWFhSk1NrfJgKgAAqBksFRU30g/JAQCA2uCGfwYEAADceAgQAABgHAECAACMI0AAAIBxBAgAADCOAAEAAMYRIAAAwDgCBDXK3r17df/996tDhw564oknnDJD7969tWzZMqe8N4ALBg8erKeeesrZY+A6qhWfhIraIykpSRaLRZs2bZK3N/8kOgDUVgQIapTCwkIFBwerRYsWzh4FAHAdcQsGNUbv3r21c+dObdy4UW3btlVWVpYyMjLUp08fhYSEqE+fPlqzZo1sNpsk6YcfflDbtm314Ycfqn///urYsaP69eunL774QuvXr9ddd92lLl26aNKkSSopKbG/T0ZGhh544AGFhISoU6dOGjx4sPbu3XvZuT777DMNGjRIISEh6tWrl2bPnq2zZ89e9z8P4EbRtm1bbdq0SY8++qhCQkIUGRmpbdu2adu2bbr33nvVqVMnjRgxQidPnrTvs23bNj300EPq3LmzOnbsqAcffFA7duy47HscPHhQI0eOVOfOnXXnnXdq0qRJOn78uInDw3VCgKDGeOONN9S5c2f16dNHH3/8sb777jvNnz9fcXFxeueddzR+/HglJycrMTGx0n7PPvusJk+erI0bN8rDw0OPPfaY3nvvPa1YsULPP/+8PvjgA61fv16StHnzZs2cOVNDhw7Ve++9pzVr1qi4uFjTpk275Ew5OTkaOnSo7rjjDr311ltKTEzU3r17FRsbK/4ZJeA/5syZo0GDBmnTpk1q1aqVJk2apJdeekkLFizQihUrtGfPHiUnJ0uSvvrqK8XFxemee+7RW2+9pfXr18vX11eTJ09WaWlpldc+duyYHnnkEQUEBOiNN97QihUrdPbsWT300EM6f/686UPFNUKAoMZo2LChbrnlFnl4eKhx48ZKSkrSqFGjdP/99ysgIED33nuvJkyYoLVr11a6ojFs2DD16NFDgYGBeuCBB3T69GnNnDlTbdu21T333KPg4GDt379fklS/fn3NmTNHDzzwgJo1a6bQ0FANGDBAX3/99SVnSk1NVffu3TVmzBi1aNFCXbt21cKFC/Xll19q586dRv5cgBtBVFSU7r33XjVv3tweBhMmTFBISIjCw8N1xx132M9Dq9Wq6dOnKzY2VgEBAQoKCtKjjz6qgoICFRQUVHnt1157TU2aNNGMGTMUGBioDh06aPHixTpx4oTef/9904eKa4RnQFAjnTx5Unl5eVqyZImWL19uX26z2VRSUqIffvhB7u7ukqSWLVva13t6ekqSAgIC7Mvc3d3t/6sqLCxMDRs2VFJSknJzc3Xo0CHt27fPflvn/8rOzlZubq46d+5cZd3BgwfVrVu3qz9YoBb43+ehh4eHpMufh+3atVO9evWUnJysQ4cO6bvvvtO+ffskSeXl5VVeOzs7WwcPHqxyHpaUlOjgwYPX/FhgBgGCGuliEEydOlU9evSost7f31/5+fmSJFfXqt/GLi6Xvrj3zjvvaMqUKbr//vsVEhKiBx98UPv379ezzz572Tn69eun0aNHV1nXsGHDah8PUNtd6jy0WCyX3HbXrl2KjY1Vz5491bVrV/Xt21dFRUWKi4u75PY2m03h4eGaOXNmlXV169a9usHhNNyCQY3k6+srX19fff/997r11lvtv/bu3avFixc7/LorVqzQgw8+qPnz52vQoEEKCwvT4cOHJemSz3S0bt1a33zzTaUZysvLNW/ePB09etThOYCbWWpqqrp166bly5fbn7G6eD5d7jw8ePCg/P397edhvXr1NHfuXPttHdx4CBDUSBaLRSNGjNDf//53/f3vf9f333+vLVu2aPbs2XJzc5Obm5tDr+vv76/PPvtMe/fu1ffff6/Vq1dr7dq1knTJh99iY2O1b98+zZgxQwcOHNCXX36pyZMn69ChQ/yoMOAgf39/ff3119q9e7d++OEHZWRkaMmSJZIufR4+8sgjOnPmjCZOnKh9+/YpJydHkyZN0p49e9S6dWvT4+MaIUBQY8XGxmrq1Klat26d7rvvPj333HPq37+/nnvuOYdf85lnnlGjRo0UExOjAQMG6H/+53/0wgsvSJK+/PLLKtt36tRJKSkp2r9/v/r376/HHntMAQEBWrVqlcMRBNzsxo0bp06dOmn06NF64IEHtH79es2dO1ceHh7as2dPle0DAgK0du1aFRUV6ZFHHlFMTIwsFovWrFkjX19fJxwBrgVLBT9LCAAADOMKCAAAMI4AAQAAxhEgAADAOAIEAAAYR4AAAADjCBAAAGAcAQIAAIwjQAAAgHEECAAAMI4AAQAAxhEgAJxu7969GjJkiG6//XZ17txZQ4cOrfRv8+zevVsxMTEKDQ3V7373Oz355JM6efKkJKm8vFwPPvigwsPD7cskadq0aQoJCdGBAweMHw+AX0aAAHCqs2fPasSIEWrQoIGWLl2qRYsWqaioSMOHD9eZM2e0a9cuDR06VB4eHlq8eLGefvpp7dy5U48++qiKi4tltVo1f/58nT9/XvPnz5ckbd++XW+88Ybi4+PVqlUrJx8hgEtxdfYAAG5uBw4c0MmTJzV48GDdfvvtkqTbbrtNaWlpOnv2rBYuXKiWLVvq5ZdfltVqlSSFhoaqb9++ysjI0KBBgxQYGKgnnnhCL7zwgu6++27Nnj1bERERiomJceahAbgC/jVcAE517tw53X333SovL1efPn3Us2dPde/eXZ6enioqKlKXLl00fPhwjR8/vtJ+UVFRCggIUFJSkiTJZrNp0KBB+uKLL1SvXj29/fbbaty4sROOCEB1cAUEgFPVqVNH69at00svvaR3331XaWlp8vT01J/+9CfFxcXJZrMpOTlZycnJVfZ1d3e3/97FxUV/+tOf9Nlnn6lDhw7EB1DDESAAnO62227TggULVF5erj179ujNN9/Ua6+9piZNmshisWjo0KHq27dvlf08PT3tvz9x4oSWLFmidu3a6aOPPtLbb7+tfv36mTwMAL8CD6ECcKr3339f4eHhOn78uKxWqzp37qxZs2bJx8dHJ0+eVHBwsL799lt17NjR/qt169Zavny5srKy7K8zc+ZMSdLKlSt17733as6cOcrPz3fWYQH4BQQIAKfq0qWLbDab4uLitGXLFmVmZmrGjBk6c+aM7rnnHk2cOFEff/yxJk2apA8//FDbtm3TiBEjtGPHDrVv316StHHjRm3ZskXTpk1Tw4YNNW3aNJWXl+uZZ55x8tEBuBweQgXgdHv27NGSJUv01VdfqaioSK1bt9bo0aMVGRkpScrMzNTy5cv11Vdf6ZZbblH79u01duxYde3aVceOHdP999+vTp06VXpO5NVXX9Xs2bM1d+5cRUdHO+vQAFwGAQIAAIzjFgwAADCOAAEAAMYRIAAAwDgCBAAAGEeAAAAA4wgQAABgHAECAACMI0AAAIBxBAgAADCOAAEAAMYRIAAAwDgCBAAAGPf/AIes26D/QmCEAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'sex' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.countplot(x='sex',data=Insurance_Data, hue='sex', palette='viridis', legend=False)\n",
    "plt.title('Sex Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "436e1463-5a23-4a43-bfd4-c2d60551e798",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sex\n",
       "male      676\n",
       "female    662\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Displaying the count of each category in the 'sex' column\n",
    "Insurance_Data['sex'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "126406a8-946c-4baa-bae3-f137fad6babd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_7868\\2638459316.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(Insurance_Data['bmi'])\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiQAAAImCAYAAABjO5F7AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAB3DklEQVR4nO3deXxU9d0+/Ouc2bNM9j0kQFhCIgQiQVAWN1qX2nKjbW8rFatFqxZuUWmxqIDSUn9iaRGxVbF0eVrUat2XgtZdgSCr7CSEhOzrJJl9znn+mMzIkARCMjNnluv9ek3BM+dkPnMaJle+qyDLsgwiIiIiBYlKF0BERETEQEJERESKYyAhIiIixTGQEBERkeIYSIiIiEhxDCRERESkOAYSIiIiUhwDCRERESmOgYSIIkIorPEYCjUQhSsGEqII9uMf/xhjx471eUyePBk333wztm/f7nPu0qVLMXbsWMycObPfH6xr1qzB2LFj8eMf/9h77Mknn8TYsWPPWofna3sehYWFmDhxIr7zne/gqaeegs1m61X36a9xLjt37sQdd9xxzvPOrPV8X+dsnn76aWzcuLHf1yKis1MrXQARBVZRURGWL18OAHC5XGhra8M///lP3HbbbXjllVcwevRo77miKKKhoQE7d+7E5MmTe32td955Z9B1pKWlYf369QAASZLQ2dmJHTt24Omnn8Znn32GP//5z9DpdADgrXegXnrpJRw7duyc533/+9/HjBkzzr/4Afj973+Pn//850F5LaJIxEBCFOHi4uIwceJEn2MXX3wxpk2bhldeeQW//OUvvcezsrIgyzLefffdXoFk9+7dqK+vx5gxYwZVh1ar7VXHrFmzUFJSgp///Od4/vnnceeddwIARo0aNajXOJfMzExkZmYG5Gsr+VpEkYBdNkRRyGAwQKfTQRCEXs9dddVVeO+99yBJks/xt99+GxdffDESExP9Wsvs2bMxYcIEbN682XvszK6Uzz//HD/84Q8xadIklJWV4a677kJFRQUAd3fQv//9b5w6dQpjx47FK6+8gpqaGowdOxZ//vOfcfXVV2PKlCl45ZVX+u1Geeqpp3DxxRdj0qRJuOuuu1BdXe19rr9rxo4diyeffNL7dwBYv3699+99Xff2229j7ty5mDRpEi655BI8/PDD6Ojo8Hmt2bNn48MPP8R1112HCy64AN/+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",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'bmi' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.distplot(Insurance_Data['bmi'])\n",
    "plt.title('BMI Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f1a0a24a-d150-47be-913a-ce99cd85b770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiAAAAImCAYAAABq0DEBAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA7QElEQVR4nO3de1xVdb7/8ffeEAIiCcjFNMvBlCEVaWSiSdLBmM7kQ88hzxynwlKTNB3JSsySUk9eaiTx0jiloFnWQKXHKaeb1UyNZYT+shta6RiVihiCpHJxX35/+GBPOzBlo98F+no+Hjwesi6bz16SvFprsbfN7Xa7BQAAYJDd6gEAAMD5hwABAADGESAAAMA4AgQAABhHgAAAAOMIEAAAYBwBAgAAjCNAAACAcQQIgPNSW3gNxrYwA2AVAgRoYz755BNlZ2dryJAh6t+/v4YOHaqcnBx98803XtuNHj1ao0eP/snHWrZsmfr06dOqfawwevRo9enTx/MRFxenxMRE3XDDDXr66afldDq9tk9NTdWMGTNO+/HffPNN3XvvvafcbsaMGUpNTfX565xMQ0ODFixYoJdeeumkXws41/lbPQCAf3vmmWc0f/58XXnllbrnnnsUFRWlr7/+Wvn5+Xr99de1evVqXX755af9eL/73e+UkpJyFic+e+Lj4zVr1ixJktPp1OHDh/X2229r/vz52rZtm/Ly8mSz2SRJjz32mEJCQk77sZ988snT2m7SpEm65ZZbWjz7qVRUVOjJJ5/UggULzvrXAtoqAgRoI7Zt26Z58+bp5ptv1syZMz3Lr7zySg0dOlQ33HCD7rvvPr344oun/ZgxMTGKiYk5G+OedSEhIRowYIDXstTUVPXs2VMLFixQamqqRowYIelErJwNPXr0OCuPa/XXAtoCLsEAbURBQYE6deqku+++u8m68PBwzZgxQ7/5zW905MgRz3K3262VK1d6LteMGjVKn3zyiWf9qS6n1NfXa8GCBbr66quVmJio++67T/X19V7bzJgxQ7feeqtmzZqlgQMHKj09XQ6HQy6XSytWrFBaWpr69u2r6667Tk8//bTXvqNHj9bMmTO1YsUKDRkyRP369dPvf/97ffTRR74eJo0ePVpRUVEqLCz0LPvxpZGXX35ZI0aMUP/+/ZWcnKxp06apoqLCs/8HH3ygDz74QH369FFxcbGKi4vVp08fFRYW6te//rV+9atfafPmzc1eFjl+/Ljmzp2rpKQkJSUl6d5779WhQ4e8jteP9/n222/Vp08frV+/Xt9++62GDh0qSbrvvvs82/54P6fTqWeeeUbDhw9X//79NWTIEOXm5nr9/cyYMUNjxozRunXrdN1116lv374aMWKE3n77bZ+PL2AKZ0CANsDtdmvz5s1KTU1VUFBQs9v8x3/8R5Nl27ZtU0NDgx544AE1NDTokUce0cSJE/X222/L3//U/3lnZ2frnXfe0dSpU9WzZ08VFRV53ZfQaOvWrbLZbFq2bJmOHj0qf39/Pfjgg1q/fr0mTJigxMRElZSUaP78+aqpqdHkyZM9+7722muKjY1VTk6O3G63HnnkEWVlZemtt96Sn59fC47SCX5+frrqqqv08ssvy+FwNHme27Zt07Rp0zRp0iQlJSWpvLxcCxcu1D333KOnn35as2bNUnZ2tiRp1qxZ6tWrlz777DNJUl5enubMmaP6+noNGDBAGzdubPL1X3nlFfXv318PP/ywDh06pNzcXJWVlXkF0U+JiorSY489pj/84Q+644479Jvf/KbZ7R588EFt2LBB48eP1y9/+UuVlpbqT3/6k3bs2KH8/HzP5adPP/1UFRUVysrKUkhIiJYsWaKsrCy98847uvDCC0/7uAKmESBAG1BVVaX6+np17969RfsFBARoxYoV6ty5syTpyJEjysnJ0a5duxQXF/eT+3755Zd67bXX9OCDD+rmm2+WJKWkpGj48OHatWuX17YOh0Nz5szRJZdcIknas2ePnnvuOd199926/fbbJUmDBg2SzWbTE088oZtuuklhYWGefQsKCjz3aBw9elT33nuvduzYob59+7bo+Tbq0qWLjh8/rurqanXp0sVr3bZt29ShQwdlZmaqQ4cOkqTOnTvrk08+kdvtVq9evTyz/PgSz+9///tmQ++HQkNDlZ+f73mMsLAwTZ48WZs3b9agQYNOOXtAQIB+/vOfSzpx2aW5y0e7du3SCy+8oKlTp+qOO+6QJF199dWKiorS9OnT9c4772jw4MGSpO+//17r16/3XMIJDg5WRkaG3n//fV133XWnnAewCpdggDbAbj/xn+KPf7vjVHr16uWJD0megPn+++9Pue/WrVslyXM5oHGO5n5oBQYGet2j8P7778vtdis1NVUOh8PzkZqaqvr6em3bts1rxh/eIBodHS1Jqq2tPc1neXKNZwF+KCkpSXV1dRo+fLjy8vK0bds2DRo0SH/4wx+a3f6HTue3fwYPHuz1fFJTU3XBBRfovffea/kTOIkPPvhAkjR8+HCv5cOGDZOfn5+Ki4s9y8LDw73+bhrv+TkTxxc4mzgDArQBnTt3VseOHbVv376TbnPs2DE1NDR4BUdwcLDXNo0h43K5Tvk1Dx8+LOnED7AfioyMbLJtRESE1w/v6upqSSd+IDbnwIEDnj//+JJSS2Y8mQMHDigwMNDrWDRKTEzUihUr9OSTT6qgoECPP/64IiMjlZmZqVtvvfUnHzciIuKUX/vHZ1zsdrs6d+6smpqaFj2Hn9L4d/Pjvwt/f3+FhYV5BeaPj2/j31Nrji9gAgECtBGDBg1ScXGx6uvrPZcOfmj9+vWaN2+enn32WSUmJrb66zVeIvnuu+900UUXeZY3xsVPCQ0NlSStWbNGHTt2bLL+h493pjmdTn3wwQe64oorTnoPSUpKilJSUlRbW6v3339fTz31lObPn68BAwYoISGhVV//x6HhdDpVVVXliRebzdbkTNaxY8da9DUa7904ePCg12W548ePq6qqyvN3B7RnXIIB2ohx48apurpaeXl5TdZVVlYqPz9fl1xySZP7FnyVnJwsSXr11Ve9lv/9738/5b5JSUmSTty70q9fP89HdXW1Fi9efFoR46vCwkJVVFToxhtvbHb9I488ov/+7/+W2+1WUFCQfv3rX3tedGz//v2S/n0WxhfvvfeeHA6H5/PXXntNDodDV155pSSpY8eOnnt6Gv2///f/vB7jVDff/vKXv5SkJjcE/+1vf5PT6dQvfvELn+cH2grOgABtxIABA3TnnXdq8eLF2r17t9LT0xUWFqYvv/xSq1at0tGjR7VixYpT3sdwui655BKNGjVKeXl5cjgc+vnPf66//vWv+vzzz0+5b+/evTVixAg98MAD2rt3r/r27as9e/YoLy9P3bt316WXXtrq+Y4cOaLt27dLOnE5oaqqSps3b1ZRUZFGjBhx0t8eueqqq7R69WrNmDFDI0aM0PHjx5Wfn6/OnTt7ois0NFQffvihtmzZ0uLXEPnuu+80ZcoUjR49Wl999ZUWLVqkq6++WldddZUk6de//rWefvpp3X///frd737n+fv7YXR06tRJkrRlyxbFxsY2OSvTq1cvpaen67HHHlNdXZ2uvPJK7dixQ4899piuvPLKdvvicsAPESBAG3LHHXcoPj5ezzzzjBYsWKDq6mrFxMTommuu0cSJE8/4pY1Zs2apS5cuWrt2rQ4fPqyUlBRNnDhRixcvPuW+CxYs0BNPPKHCwkKVl5crIiJC119/vaZOnerTr9f+WGlpqUaNGiXpxBmLiIgI9ezZUw8//HCTmzN/6JprrlFubq5WrVrlufH0F7/4hZ566inPPSM333yzPv30U2VmZmrBggWKioo67bn+53/+R3V1dZo8ebICAgI0fPhwZWdne8Lw6quv1r333qunn35ar7/+ui6//HI99thj+v3vf+95jJCQEI0dO1ZFRUX6xz/+oXfffbfJ15k3b54uueQSrVu3TgUFBYqKitLo0aM1efLkVp3BAdoKm5t3QwIAAIaR0QAAwDgCBAAAGEeAAAAA4wgQAABgXJsIkA0bNuj6669Xv379NGzYML3yyiuedTt27FBGRoYGDBigIUOGqKCgwGtfl8ulpUuXKiUlRQkJCRo3bpzKyspMPwUAANAClgfIX//6V91///0aNWqUNm7cqOuvv1533323PvzwQ1VVVWns2LG69NJLtW7dOk2ZMkVLlizRunXrPPsvX75chYWFmjt3roqKimSz2ZSZmamGhgYLnxUAAPgplv4artvt1tChQ3Xdddd5XqlQkm677TbPKwE+88wzeuuttzxvub1o0SK9/vrrevXVV9XQ0KDk5GRlZ2d7XhWxpqZGKSkpmj9//knfpwIAAFjL0hci+9e//qW9e/c2eVGhxsssmZmZSkpK8sSHdOLlo5944glVVlZq7969Onr0qOfVDaUTr3AYHx+vkpISnwPE7XbL5eLlUQAAaAm73Xbar9ZsaYB89dVXkk68UdNtt92m0tJSde/eXXfccYdSU1NVXl6u3r17e+3T+IqF+/btU3l5uSSpa9euTbZpfM8HX7hcbtXU8FbWAAC0RGhokPz82kGAHDlyRJJ077336g9/+IOmTZum1157TZMmTdLq1atVV1engIAAr30a3yW0vr5etbUnIqG5bRrfztoXdrtNYWFN3+ETAACcGZYGyAUXXCDpxD0f6enpkqSf//znKi0t1erVqxUYGNjkZtLGd5gMDg5WYGCgJKmhocHz58ZtgoKCfJ7rxBmQlr19NgAA57sTZ0BO7/dbLA2QmJgY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RYs0ZcoUvfXWW4qIiDjl4y9cuFBPPfWUJk6cqAEDBujVV1/Vo48+2mS7ffv2adOmTVq0aJGqqqoUFhamJ554Qnl5ecrIyNB9992nHTt2aNmyZdq/f7/mz5/v2ffTTz9VRUWFsrKyFBISoiVLligrK0vvvPOOLrzwwjN3sABIIkAAtFJNTY1Wr16t0aNHa/r06ZKkq6++WocOHdK2bdsUFRUll8ulP/3pT4qNjZUkdejQQWPHjtX27ds1dOjQUz7+008/rVtuuUVTpkyRJKWkpOjAgQP65z//6bWtw+HQvffeq1/96leSpO+//15//vOfNWrUKOXk5EiSBg0apM6dOysnJ0djx47VZZdd5tl2/fr16tGjhyQpODhYGRkZev/993XdddedoaMFoBGXYAC0yvbt23X8+HGlpaV5LZ8xY4ZWrVolSQoLC/PEhyRdfPHFkk780D/dx/9xqPz2t79tdvvevXt7/vzhhx+qtrZWqampcjgcno/G37B59913PduGh4d74kOSYmJiJEm1tbWnnBFAy3EGBECrVFdXS9JP3kQaHBzs9bnNZpN04t6OU2m81+PHjx8ZGdns9l26dGky2+23397sthUVFZ4/BwUF+TwjgJYjQAC0SmhoqCTp0KFD+tnPfuZZvn//fpWVlen48eOtevywsDBJUmVlpdfjN8bF6cyWm5urSy+9tMn6H8YKALO4BAOgVfr3768LLrhAb775ptfyNWvW6M477/ScSfBVYmKiAgMD9eqrr3ot//vf/37KfRMSEnTBBRfowIED6tevn+fjggsu0KOPPsqLmAEW4gwIgFYJDw/XLbfcojVr1iggIEDJycn65JNPtHbtWt1999364osvWvX4HTt21KRJk7R48WIFBQUpOTlZb7/99mkFSFhYmMaPH68lS5boyJEjuvLKK3XgwAEtWbJENptNcXFxrZoNgO8IEACtlp2drS5duugvf/mLVq1ape7du+v+++/XTTfdpBkzZrT68SdMmKDg4GCtWbNGa9asUWJiou69917Nnj37lPtOnTpVkZGRevbZZ5Wfn68LL7xQV111le6++2516tSp1bMB8I3N/cNXCgIAADCAe0AAAIBxBAgAADCOAAEAAMYRIAAAwDgCBAAAGEeAAAAA4wgQAABgHAECAACMI0AAAIBxBAgAADCOAAEAAMYRIAAAwLj/D+t/4oX9oTMFAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'children' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.countplot(x='children',data=Insurance_Data, hue='children', palette='viridis', legend=False )\n",
    "plt.title('Children Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "617a331f-08e1-4da8-b476-15b7cdba8de6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "children\n",
       "0    574\n",
       "1    324\n",
       "2    240\n",
       "3    157\n",
       "4     25\n",
       "5     18\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Displaying the count of each category in the 'children' column\n",
    "Insurance_Data['children'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "2ff3b684-3a70-4c54-9d6a-bc644daa0f6f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAigAAAImCAYAAAB5B3H1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAA2KElEQVR4nO3dfVjV9f3H8dc5MARFFBBFLVMpdZQgKItKfvCzaEuzQmouw6l4t2SYmpqGP2NL7UYKQdOZ4E2rBTZMu3NNW62mZlqpu0JnGmOWoqQI3iDIOfz+8PKsE1gIyPkgz8d1eQXfu/M+6IFn3+8XsFRXV1cLAADAIFZXDwAAAPB9BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAPAdJvzsShNmAFyNQAGaqf3792vq1Km67bbbdNNNN2ngwIGaMmWK8vPzm2yGxYsXq3fv3k3+eN/9ExISojvvvFPPPPOMysrKnLafNWuWBg0aVOfjHzhwQA8++OCPbrdu3Tr17t1bX3/9db0e54e89tpreuaZZy75WEBL4e7qAQBcvi+//FLDhw9XSEiIUlJS1KFDBxUVFenll1/W8OHD9cc//lH9+vVz9ZhXTG5urqQLZxrOnj2rf/7zn1qxYoXef/99vfrqq/L19ZUkTZo0Sb/+9a/rfNyNGzfq888//9HtYmJilJubq44dO9bvCfyAZcuW6Wc/+1mTPBZgMgIFaIZWrVql9u3bKysrSz/5yU8cy++44w7dddddWrp0qV588UUXTnhlfT++brvtNt1yyy166KGH9Nxzz2nevHmSpG7dul2Rx/fz85Ofn98VObYrHwswCZd4gGbo22+/lVTzXoXWrVtr9uzZuuuuuxzLRo4cqblz52rZsmWKiopSaGioxo8fr2+//VZ5eXmKjY1VWFiYRo8eXeMywjvvvKNhw4YpLCxMt912m+bOnavS0tJLznX48GHFxMQoLi7OsV1FRYWeffZZRUdH66abbtLQoUP1zjvvOO03aNAgLViwQKNGjVJ4eLjmzp172R+T0NBQ3XHHHVq/fr3Ky8sl1bz08sUXX2jUqFHq37+/4znv3r1b0oXLR0uWLJEk9e7dW4sXL3a8vWTJEsXHx6t///5aunTpJS+75ObmKiYmRiEhIRo1apTT5bZL7TNo0CDNmjXL8fY333yj119/3bFtbftt2bJFI0aMUP/+/XXzzTfr0Ucf1ZEjR5weKzg4WLt379bw4cPVt29fxcTEaMWKFZf9cQVchUABmqGYmBgdPnxYv/rVr/TKK6/o4MGDjlj5xS9+obi4OKft3377bW3dulXz58/X7NmztXXrViUkJOiPf/yjHnvsMaWkpGj37t36/e9/79hn6dKlmjp1qkJDQ5WZmamkpCS9++67GjlypM6dO1djpuLiYo0ePVrt2rXTypUr1a5dO1VXVyspKUk5OTkaM2aMli1bprCwME2dOlXr16932v+VV15xhMG9995br4/LwIEDdf78ef3zn/+sse706dMaN26cfH19lZmZqfT0dJWXl2vs2LE6deqUHnjgAd1///2SLoTGAw884Nh32bJl+vnPf67nn39et99+e62PXVRUpMWLF2vKlCl6/vnnVVpaql//+tc6ceJEnedfsmSJAgICFB0dfcnLOhs2bFBiYqI6deqk559/XrNnz9bnn3+u4cOH6/jx447t7Ha7pkyZosGDB+vFF19U//79lZaWpo8++qjO8wCuxCUeoBkaMWKEiouLlZ2d7YgKX19fDRw4UCNHjlRoaKjT9ufPn9eSJUvUrl07SdKmTZv0j3/8Q5s3b9a1114rSdq7d682bNggSSotLdWyZcv0wAMP6IknnnAcp1evXnrooYe0bt06jRgxwrG8pKREiYmJ8vT01OrVqx33gGzdulUfffSR0tPTNXjwYElSVFSUysvLlZaWprvvvlvu7hc+DXXs2FGzZs2S1Vr//28KCAiQ9N8zTN914MABnThxQiNHjlT//v0lST179lROTo5Onz6tzp07KzAwUFLNS0ghISGaMGGC4/0vvviixvFtNpuWLFni2PfiGZ3Vq1dr2rRpdZo/ODhYHh4e8vPzq/UeIrvdroULF+rWW29Venq6Y3l4eLgGDx6slStXasaMGZIunF2bNGmSI7T69++vTZs26YMPPlBUVFSd5gFciTMoQDP1yCOP6KOPPtJzzz2n+++/X97e3nrzzTc1fPhwrVmzxmnboKAgR5xIF76Q+/n5OeJEktq3b69Tp05Jknbt2qXKykoNHTrU6TgDBgxQ165dtX37dqfl48aN0/79+zV79mxHnEjStm3bZLFYFB0draqqKsefQYMGqbi4WF9++aXTjA2Jkx9zww03yM/PTw8//LCeeOIJ/e1v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CBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGKdZBMr58+eVnp6umJgYhYWFacSIEfrss88c6/fu3auEhAT169dPMTExys7OdtrfbrcrMzNTUVFRCg0NVWJiogoLC5v6aQAAgDpqFoGybNky5eXlad68eVq/fr169uyp8ePH6+jRoyopKdGYMWPUvXt35eXlKTk5WRkZGcrLy3Psv3TpUuXk5GjevHnKzc2VxWLR+PHjVVlZ6cJnBQAALqVZBMp7772nu+++WwMHDtR1112nWbNm6fTp09q1a5fWrl0rDw8PpaamKigoSPHx8Ro9erRWrFghSaqsrNTKlSuVnJys6Oho9enTR+np6Tp69Kg2bdrk4mcGAABq0ywCpX379nr//ff19ddfy2azKTc3Vx4eHvrpT3+qnTt3KiIiQu7u7o7tIyMjVVBQoOPHj2vfvn06c+aMIiMjHet9fHwUHBysHTt2uOLpAACAH+H+45u4XkpKiqZOnarbb79dbm5uslqtysjIULdu3VRUVKRevXo5bd+xY0dJ0uHDh1VUVCRJ6ty5c41tjhw50qC53N2bRd8BaERubrzu0XK48t97swiUgwcPysfHRy+88II6deqk1157TY899phefvllnTt3Th4eHk7bt2rVSpJUUVGh8vJySap1m9LS0nrPZLVa5Ovbpt77AwBgOh8fL5c9tvGB8s0332jGjBlavXq1BgwYIEnq27evDhw4oMWLF8vT07PGza4VFRWSpNatW8vT01PShXtRLr59cRsvr/p/4O32apWVna33/gCaJzc3q0s/aQNNqaysXDabvVGP6ePjVaczM8YHyp49e3T+/Hn17dvXaXloaKg+/PBDdenSRceOHXNad/H9Tp06qaqqyrGsW7duTtv06dOnQbNVVTXuXxoAACax2ewu+1pn/MXUi/eO/Otf/3Javn//fl133XWKiIjQp59+KpvN5li3bds29ejRQ/7+/urTp4+8vb21fft2x/qysjLl5+c7zsgAAACzGB8oISEhGjBggB577DF9/PHH+ve//61FixZp27ZtmjBhguLj43X69GmlpKTowIEDWrdundasWaOJEydKunDvSUJCgtLS0vTee+9p3759mjp1qgIDAxUbG+viZwcAAGpj/CUeq9WqpUuXatGiRZo9e7ZKS0vVq1cvrV69Wv369ZMkZWVlaf78+YqLi1NAQIBmzpypuLg4xzEmT56sqqoqzZkzR+fOnVNERISys7Nr3DgLAADMYKmurq529RDNkc1m14kTZ1w9BoAm5u5ula9vG016d7EOlBx29TjAFXG9bxct/XmySkrONPo9KH5+bep0k6zxl3gAAEDLQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOM0mUNavX6/Bgwerb9++GjJkiDZu3OhYt3fvXiUkJKhfv36KiYlRdna20752u12ZmZmKiopSaGioEhMTVVhY2NRPAQAA1FGzCJQNGzbo8ccf1/Dhw/XWW29p8ODBmjZtmj7//HOVlJRozJgx6t69u/Ly8pScnKyMjAzl5eU59l+6dKlycnI0b9485ebmymKxaPz48aqsrHThswIAAJfi7uoBfkx1dbUyMjI0atQojRo1SpKUlJSkzz77TJ988ok++eQTeXh4KDU1Ve7u7goKClJhYaFWrFih+Ph4VVZWauXKlZoxY4aio6MlSenp6YqKitKmTZs0ZMgQVz49AABQC+PPoHz11Vf65ptvNHToUKfl2dnZmjhxonbu3KmIiAi5u/+3tSIjI1VQUKDjx49r3759OnPmjCIjIx3rfXx8FBwcrB07djTZ8wAAAHVXrzMo69evV3R0tHx9fWusKy4u1vr16zV+/PgGDydJ//73vyVJZ8+e1dixY5Wfn69rrrlGDz/8sAYNGqSioiL16tXLaZ+OHTtKkg4fPqyioiJJUufOnWtsc+TIkQbN5u5ufN8BaGRubrzu0XK48t97vQJl9uzZys3NrTVQ9u7dq8zMzEYLlNOnT0uSHnvsMf32t7/V9OnT9e6772rSpElatWqVzp07Jw8PD6d9WrVqJUmqqKhQeXm5JNW6TWlpab3nslot8vVtU+/9AQAwnY+Pl8seu86BMnHiRB04cEDShftCkpKSanzRl6Tjx4+rW7dujTbgT37yE0nS2LFjFRcXJ0n66U9/qvz8fK1atUqenp41bnatqKiQJLVu3Vqenp6SpMrKSsfbF7fx8qr/B95ur1ZZ2dl67w+geXJzs7r0kzbQlMrKymWz2Rv1mD4+XnU6M3NZgfLaa69Jkl5//XUFBwfLz8/PaRur1SofHx8NGzbsMse9tMDAQEmqcRnn+uuv1wcffKCuXbvq2LFjTusuvt+pUydVVVU5ln03nI4dO6Y+ffo0aLaqqsb9SwMAwCQ2m91lX+vqHCjh4eEKDw93vD9p0iRde+21V2So7woODlabNm20e/duDRgwwLF8//796tatm8LDw5WTkyObzSY3NzdJ0rZt29SjRw/5+/urbdu28vb21vbt2x2BUlZWpvz8fCUkJFzx+QEAwOWr1z0oTz31VGPPcUmenp4aN26cXnjhBXXq1EkhISF6++23tWXLFq1evVrXX3+9srKylJKSonHjxmnPnj1as2aNfve730m6cO9JQkKC0tLS5Ofnp65du2rhwoUKDAxUbGxskz0PAABQd/UKlBMnTmj+/Pn64IMPVF5erurqaqf1FotF+fn5jTKgdOFsjZeXl9LT03X06FEFBQVp8eLFuvnmmyVJWVlZmj9/vuLi4hQQEKCZM2c67leRpMmTJ6uqqkpz5szRuXPnFBERoezs7FrvoQEAAK5nqf5+XdTB5MmT9fe//11DhgxRYGCgrNaaN7v89re/bZQBTWWz2XXixBlXjwGgibm7W+Xr20aT3l2sAyWHXT0OcEVc79tFS3+erJKSM41+D4qfX5vGvUn2uz766CPHj54HAABobPX6CSweHh5NcoMsAABomeoVKLGxsXrrrbcaexYAAABJ9bzEExwcrEWLFunQoUMKDQ11+gFo0oWbZJOSkhplQAAA0PLUK1B+//vfS5J27NhR6y/cI1AAAEBD1CtQ9u3b19hzAAAAOPBrOQEAgHHq/duMf0xT/rRZAABwdalXoGzfvr3GsrNnz+rkyZNq3769+vbt2+DBAABAy1WvQPnb3/5W6/KvvvpKycnJuu+++xoyEwAAaOEa9R6Unj17KikpSUuWLGnMwwIAgBam0W+S9fb21jfffNPYhwUAAC1IvS7xHD5c8xdk2Ww2FRUVadGiRQoKCmrwYAAAoOWqV6AMGjRIFoulxvLq6mp5eXlp8eLFDR4MAAC0XPUKlAULFtQIFIvFIm9vb0VGRsrb27tRhgMAAC1TvQJl2LBhjT0HAACAQ70CRZJOnDihVatWafv27SorK5Ovr68GDBig0aNHy9/fvzFnBAAALUy9vounqKhIcXFxWr16tVq1aqXg4GC5u7tr1apVuu+++3T06NHGnhMAALQg9TqDsnDhQrm7u+udd97Rtdde61h+6NAhJSYmKj09XU8//XSjDQkAAFqWep1B+cc//qHJkyc7xYkkXXvttUpKStKHH37YKMMBAICWqV6BYrPZ5OvrW+s6Pz8/nT59ukFDAQCAlq1egdK7d29t2LCh1nXr169Xr169GjQUAABo2ep1D8qkSZM0duxYnTx5UkOHDlWHDh307bff6s0339TWrVuVmZnZ2HMCAIAWpF6Bctttt+nZZ5/Vs88+qy1btjiWBwQE6KmnnlJsbGyjDQgAAFqeev8clG+++Ua9e/fWmjVrVFpaqn379ikjI0MnT55sxPEAAEBLVK9AycrK0pIlS/TrX//a8YsBu3Tpov/85z967rnn5OXlpeHDhzfqoAAAoOWoV6CsXbtWU6dO1bhx4xzLAgMDNWvWLPn5+emll14iUAAAQL3V67t4jh49qhtvvLHWdX379tXXX3/doKEAAEDLVq9Aufbaa7V169Za123fvl2BgYENGgoAALRs9brE8+CDD2rBggWqqqrSHXfcIX9/f504cUKbN2/WSy+9pOnTpzf2nAAAoAWpV6A89NBDKioq0qpVq7R69WrHcjc3N40aNUqjR49upPEAAEBLVO9vM3700Uc1YcIE7dq1SydPnpSPj49CQkIu+SPwAQAA6qregSJJbdu2VVRUVGPNAgAAIKmeN8kCAABcSQQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOM0qUAoKChQWFqZ169Y5lu3du1cJCQnq16+fYmJilJ2d7bSP3W5XZmamoqKiFBoaqsTERBUWFjb16AAA4DI0m0A5f/68pk+frrNnzzqWlZSUaMyYMerevbvy8vKUnJysjIwM5eXlObZZunSpcnJyNG/ePOXm5spisWj8+PGqrKx0xdMAAAB10GwCZfHixWrTpo3TsrVr18rDw0OpqakKCgpSfHy8Ro8erRUrVkiSKisrtXLlSiUnJys6Olp9+vRRenq6jh49qk2bNrniaQAAgDpoFoGyY8cO5ebm6plnnnFavnPnTkVERMjd3d2xLDIyUgUFBTp+/Lj27dunM2fOKDIy0rHex8dHwcHB2rFjR5PNDwAALo/xgVJWVqaZM2dqzpw56ty5s9O6oqIiBQYGOi3r2LGjJOnw4cMqKiqSpBr7dezYUUeOHLmCUwMAgIZw//FNXCs1NVX9+vXT0KFDa6w7d+6cPDw8nJa1atVKklRRUaHy8nJJqnWb0tLSBs/m7m583wFoZG5uvO7Rcrjy37vRgbJ+/Xrt3LlTb775Zq3rPT09a9zsWlFRIUlq3bq1PD09JV24F+Xi2xe38fLyatBsVqtFvr5tfnxDAACaKR+fhn2tbAijAyUvL0/Hjx9XTEyM0/InnnhC2dnZ6tKli44dO+a07uL7nTp1UlVVlWNZt27dnLbp06dPg2az26tVVnb2xzcEcFVxc7O69JM20JTKyspls9kb9Zg+Pl51OjNjdKCkpaXp3LlzTsvuvPNOTZ48WYMHD9bbb7+tnJwc2Ww2ubm5SZK2bdumHj16yN/fX23btpW3t7e2b9/uCJSysjLl5+crISGhwfNVVTXuXxoAACax2ewu+1pndKB06tSp1uX+/v7q2rWr4uPjlZWVpZSUFI0bN0579uzRmjVr9Lvf/U7ShXtPEhISlJaWJj8/P3Xt2lULFy5UYGCgYmNjm/KpAACAy2B0oPwYf39/ZWVlaf78+YqLi1NAQIBmzpypuLg4xzaTJ09WVVWV5syZo3PnzikiIkLZ2dk1bpwFAADmsFRXV1e7eojmyGaz68SJM64eA0ATc3e3yte3jSa9u1gHSg67ehzgirjet4uW/jxZJSVnGv0Sj59fmzrdg8L3ywEAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjuLt6ANRktVpktVpcPQZwRdnt1bLbq109BgBDESiGsVotat++tdzcOLmFq5vNZtfJk2eJFAC1IlAMY7Va5OZm1e+zX1fhkW9dPQ5wRVzXuYPmjo2T1WohUADUikAxVOGRb7X/UJGrxwAAwCW4jgAAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgQIAAIxDoAAAAOMQKAAAwDgECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjGB8oJ0+e1Ny5c/U///M/Cg8P14MPPqidO3c61u/du1cJCQnq16+fYmJilJ2d7bS/3W5XZmamoqKiFBoaqsTERBUWFjb10wAAAJfB+ECZNm2adu/ereeff15//vOfdeONN2rs2LE6ePCgSkpKNGbMGHXv3l15eXlKTk5WRkaG8vLyHPsvXbpUOTk5mjdvnnJzc2WxWDR+/HhVVla68FkBAIAf4u7qAX5IYWGhtmzZoldffVXh4eGSpJSUFH344Yd666235OnpKQ8PD6Wmpsrd3V1BQUEqLCzUihUrFB8fr8rKSq1cuVIzZsxQdHS0JCk9PV1RUVHatGmThgwZ4sqnBwAALsHoMyi+vr568cUXddNNNzmWWSwWVVdXq7S0VDt37lRERITc3f/bWZGRkSooKNDx48e1b98+nTlzRpGRkY71Pj4+Cg4O1o4dO5r0uQAAgLozOlB8fHwUHR0tDw8Px7KNGzfqP//5jwYOHKiioiIFBgY67dOxY0dJ0uHDh1VUVCRJ6ty5c41tjhw5coWnBwAA9WX0JZ7v+/TTT/X444/r9ttv16BBg/TUU085xYsktWrVSpJUUVGh8vJySap1m9LS0gbP4+7e+H3n5mZ0MwKNqjn+e2+OMwP15cp/780mUDZv3qzp06crNDRUzz//vCTJ09Ozxs2uFRUVkqTWrVvL09NTklRZWel4++I2Xl5eDZrHarXI17dNg44BtHQ+Pg17HQK4slz5Gm0WgfLyyy9r/vz5io2NVVpamuOMSGBgoI4dO+a07cX3O3XqpKqqKseybt26OW3Tp0+fBs1kt1errOxsg45RGzc3K5+00WKUlZXLZrO7eozLwmsULcmVeI36+HjV6cyM8YHypz/9SU8++aRGjhypxx9/XFbrf59URESEcnJyZLPZ5ObmJknatm2bevToIX9/f7Vt21be3t7avn27I1DKysqUn5+vhISEBs9WVdW8PrECprHZ7LyOAIO58jVq9MXUgoICLViwQLGxsZo4caKOHz+u4uJiFRcX69SpU4qPj9fp06eVkpKiAwcOaN26dVqzZo0mTpwo6cK9JwkJCUpLS9N7772nffv2aerUqQoMDFRsbKyLnx0AALgUo8+gvPvuuzp//rw2bdqkTZs2Oa2Li4vT008/raysLM2fP19xcXEKCAjQzJkzFRcX59hu8uTJqqqq0pw5c3Tu3DlFREQoOzu7xo2zAADAHEYHym9+8xv95je/+cFtQkJClJube8n1bm5umjFjhmbMmNHY4wEAgCvE6Es8AACgZSJQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABiHQAEAAMYhUAAAgHEIFAAAYJwWEyh2u12ZmZmKiopSaGioEhMTVVhY6OqxAABALVpMoCxdulQ5OTmaN2+ecnNzZbFYNH78eFVWVrp6NAAA8D0tIlAqKyu1cuVKJScnKzo6Wn369FF6erqOHj2qTZs2uXo8AADwPS0iUPbt26czZ84oMjLSsczHx0fBwcHasWOHCycDAAC1cXf1AE2hqKhIktS5c2en5R07dtSRI0fqdUyr1SI/vzYNnu37LJYL/02bPEJVNlujHx8wgbubmySpXTsvVVe7eJjLdPE1uiB6jKrsvEZxdXK3XrnXqNVqqdsMjfuwZiovL5ckeXh4OC1v1aqVSktL63VMi8UiN7e6fZDrw9en8eMHMI3V2nxP4rb39Hb1CMAV58rXaPP97HAZPD09JanGDbEVFRXy8vJyxUgAAOAHtIhAuXhp59ixY07Ljx07psDAQFeMBAAAfkCLCJQ+ffrI29tb27dvdywrKytTfn6+BgwY4MLJAABAbVrEPSgeHh5KSEhQWlqa/Pz81LVrVy1cuFCBgYGKjY119XgAAOB7WkSgSNLkyZNVVVWlOXPm6Ny5c4qIiFB2dnaNG2cBAIDrWaqrm9s3+QEAgKtdi7gHBQAANC8ECgAAMA6BAgAAjEOgAAAA4xAoAADAOAQKAAAwDoECAACMQ6AAAADjECgAAMA4BAoAADAOgYKr0vz583XHHXc4LTt16pRCQkL03nvv6bPPPtNDDz2kkJAQxcTE6He/+51Onz7t2HbPnj0aMWKEwsLCFBERoeTkZB0+fLipnwbQYvTu3Vtr167VmDFjFBISoqioKC1fvtxpmw8++EC//OUvFRYWpoEDB+rpp59WRUWFiybGlUag4Kp0//3369ChQ9q5c6dj2TvvvCNvb2917dpVo0eP1m233aY33nhDaWlp+uKLL5SYmKjq6mrZ7XZNnDhREREReuONN7R69WodPnxYjz/+uAufEXD1e/bZZ3Xfffdpw4YNio+P1/PPP+94DW/evFkPP/ywoqOjlZeXpyeffFIbN27U9OnTXTw1rpQW89uM0bL07t1bN954o9544w0NGDBAkvT666/r3nvvVXZ2tm655RZNmjRJktS9e3c999xzuuOOO/TJJ5+oT58+KikpUceOHXXNNdfIYrFo0aJFOn78uCufEnDVi4uL07333itJmjJliv70pz/p008/1YABA7R8+XLFxsYqKSlJktSzZ09VV1fr4Ycf1sGDBxUUFOTK0XEFcAYFV634+Hht3LhRlZWVKiws1Oeff664uDjl5+dry5YtCgsLc/y55557JEkHDx5Uu3btNG7cOD355JO69dZb9eijj+qzzz5Tnz59XPyMgKvb9yPD29tb58+flyTt379f4eHhTusjIiIkSf/617+aZkA0Kc6g4Ko1dOhQPfPMM3r//fe1f/9+9e3bV7169ZLdbtfQoUP1m9/8psY+fn5+kqTp06drxIgR+vvf/65t27YpNTVVy5cv1/r16+Xh4dHUTwVoEWp7bVVXVzv+a7FYnNbZbDZJkrs7X8quRpxBwVXLx8dHsbGx+utf/6q//vWvGjZsmCTphhtu0JdffqnrrrvO8cdms+mpp57SkSNH9NVXX+mJJ56Qv7+/HnzwQWVmZiorK0sHDx7Uvn37XPysgJapV69e+vTTT52WXbw/hcs7VycCBVe1+Ph4bd68WYWFhbr77rslSYmJidq7d6/mzp2rAwcOaPfu3Zo+fboKCgrUvXt3tW/fXm+99Zbmzp2rgwcPqqCgQHl5eWrXrp169uzp4mcEtExjx47VX//6V73wwgsqKCjQ+++/ryeffFL/+7//S6BcpTgvhqvaLbfcIl9fX4WHh8vHx0eS1K9fP2VlZSkjI0PDhg2Tl5eXIiMj9dhjj8nDw0N+fn7KysrSc889p1/+8pey2Wzq16+fVq1aJW9vbxc/I6Bluuuuu2Sz2bR8+XItW7ZMfn5+uvvuuzV58mRXj4YrxFJ98QIfcBU6e/asBg4cqCVLlujWW2919TgAgDriDAquSqWlpfr444+1ceNGdenSRbfccourRwIAXAYCBVelqqoqpaSkyM/PT4sWLapx9z8AwGxc4gEAAMbhu3gAAIBxCBQAAGAcAgUAABiHQAEAAMYhUABc9datW6fevXvr66+/dvUoAOqIQAEAAMYhUAAAgHEIFABN5osvvtCoUaPUv39/hYWFafTo0dq9e7ckadasWRo7dqzWrl2rO+64QyEhIfrVr37l+MVwQ4cOVWhoqB544AHt3bvX6bhbtmzRiBEj1L9/f91888169NFHdeTIkUvOUVZWpnvvvVeDBg1yXPax2+168cUXFRsbq5tuukk///nP9cc//tFpv5EjR2r69OmaPHmywsPDNWHChEb+CAG4iJ8kC6BJnD59WuPGjdPNN9+szMxMnT9/XsuWLdPYsWP1/vvvS5J27dqlY8eOadasWTp37pxSU1M1YcIEWSwWTZ48WVarVQsWLND06dP19ttvS5I2bNigmTNnavDgwZo4caJKSkqUmZmp4cOH6/XXX5e/v7/THGfOnNH48eNVVlaml156Sddcc40kKTU1VevWrdPEiRMVFhamHTt2aMGCBSorK1NSUpJj/40bN+oXv/iFXnjhBdlstib66AEtD4ECoEkcOHBAJ06c0MiRI9W/f39JUs+ePZWTk6PTp09LuhAxixYtUlBQkCTpk08+UW5urlavXu34fUpFRUV65plnVFZWJm9vby1cuFC33nqr0tPTHY8VHh6uwYMHa+XKlZoxY4ZjeUVFhR5++GEVFRXp5Zdf1rXXXitJKigo0Nq1azVt2jTHWZGBAwfKYrFo+fLlGjFihHx9fSVJVqtVTz75pFq3bn2FP2JAy8YlHgBN4oYbbpCfn58efvhhPfHEE/rb3/6mgIAAzZw5U507d5YktWvXzhEnkhQQECBJ6tevn2NZ+/btJV24TFNQUKDi4mINHTrU6bG6deumsLAwbd++3Wn5zJkztX37diUnJzviRJI+/vhjVVdXa9CgQaqqqnL8GTRokCoqKvTpp586tr3mmmuIE6AJcAYFQJNo06aNXnnlFS1btkzvvPOOcnJy5OXlpXvuuUcpKSmSJG9v71r39fLyqnX5yZMnJUkdOnSosa5Dhw7Kz893Wnb06FHddNNNeuGFF3TXXXepTZs2TscZMmRIrY9z9OhRp+MCuPIIFABNpmfPnlq4cKFsNpv27NmjDRs26NVXX3XcB3K5Lp5N+fbbb2usKy4udlyWuWjJkiXy9vbWfffdp/T0dM2ZM0eS5OPjI0las2aNI1q+q0uXLvWaD0D9cYkHQJP4y1/+osjISBUXF8vNzU1hYWFKTU2Vj4+PioqK6nXMHj16KCAgQG+++abT8kOHDmnXrl0KDw93Wt6hQwddf/31GjNmjF555RV9/vnnkqSIiAhJUklJifr27ev4c/LkSS1atMhxhgVA0yFQADSJ8PBw2e12JSUlafPmzdq2bZvmzp2rU6dO6c4776zXMa1Wq6ZNm6atW7dq6tSp+vvf/67169drzJgxateuncaMGVPrfklJSercubPmzJmjyspK9erVS/fcc4/+7//+T1lZWfr444/16quv6tFHH1VJSYm6d+/egGcOoD4IFABNomPHjsrKylLbtm2VkpKiiRMn6osvvtDixYsVGRlZ7+MOGzZMmZmZKiwsVFJSkp5++mmFhYXpz3/+s+Mm2+/z9PTU3LlzdeDAAf3hD3+QJD311FMaM2aMcnJyNG7cOP3hD39wfCeQm5tbvecDUD+W6urqalcPAQAA8F2cQQEAAMYhUAAAgHEIFAAAYBwCBQAAGIdAAQAAxiFQAACAcQgUAABgHAIFAAAYh0ABAADGIVAAAIBxCBQAAGAcAgUAABjn/wFAVhJOy0vdkAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'smoker' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.countplot(x='smoker',data=Insurance_Data, hue='smoker', palette='viridis', legend=False )\n",
    "plt.title('Smoker Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "33350801-6005-4280-b01a-e589583990ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "smoker\n",
       "no     1064\n",
       "yes     274\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Displaying the count of each category in the 'smoker' column\n",
    "Insurance_Data['smoker'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2a7474bf-165b-4868-b15f-e64c3312cdb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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QkJClJycrO3bt6tDhw7avHmz3nrrLUnSgQMHtG/fPq1du9a+LeP/X2s8duyYwsPDb3t8JVlx7Gt+etWtWzd9++23io+PV0JCgg4ePChJysnJkST17dtX/fv3V2hoqBo1aqTmzZurXbt2JSo83snNXzg3ubm56bfffpMkHT58WO3atcu1vmnTppKkQ4cO2Z/70EMP3XU//9vH8uXL6/Tp05JuvD6nTp2qxMRE/fTTT6pXr54iIiLslw42btxof30dOHBAx44dU6NGjXJtLyMjQ8eOHZMkDR06VJMmTdInn3yikJAQhYWF6amnnpLV+mBclS8OPc1Pn7p166YffvhBX3zxhU6ePKnDhw8rMTFRtWvXliQ988wzWr16tZ544gn5+fmpefPmioyMVLVq1fJzGhyOAOIg06dP18CBA7V582Zt27ZNw4YNU+PGjeXs7CyLxXLL+OzsbJUqVcr+2Pifm4tuvnjuxGaz3bLs5nZatmypt99+W8eOHdO2bds0fvx4JScna968edq/f78uX76ssLAwSTd+MfXp00edOnW6ZXs30//tju9vf/vbXeu8nxW3vt6tVxcuXNCf//xneXh4qHXr1goNDVVgYKDCw8Pt4xo1aqRNmzZp69atiouL0+eff645c+Zo0aJFCg0NvWt997vfh8abbp5fwzBu6evNmT4np//+eM3Pvz7z6uNNtWvXVp06dbRlyxbt27fPPms5ZswYJSQkaOvWrYqNjZV0o+chISEaO3bsLdu5GRpffPFFPfnkk9q0aZPi4uI0Y8YMzZkzR+vWrVOlSpXuWuv9rjj09G59MgxD/fv316FDh9ShQwe1bdtWw4YNs/9DULoxs/HFF1/op59+0tatW7VlyxYtWbJEgwYN0l//+te71udoD0bcLWb27t2rSZMm6eGHH1aPHj20YMECTZo0STt27JCXl5f27duX6ybBCxcuKCEhwZ68S5UqpcuXL+fa5r2+pbVy5cpq0KCBVq1apeTkZDVp0kSPPfaYTp06peXLlyskJMQ+Rf/II4/ol19+0UMPPWT/OnfunN577z1dvXr1jsdXXN+PXhiKY1/v1quvvvpKFy9e1MqVKzVgwABFRkbab5q9+QM5NjZWe/bsUevWrTVmzBh99913qlmzpr777jtJyjNYPSh8fX21Z8+eXMtufr7N//4r+/cKcs4iIiK0detWbd++XSEhIapRo4Zq1qyp999/XxaLRX/6058k3ej5sWPHVLVqVXvPy5cvr0mTJunw4cO6cOGC3nnnHf3222/q3Lmzpk2bpi+//FLnz5/Xzp07/3BdJY1ZPb1bnw4cOKBNmzYpNjZWr7/+up555hnVqlVLJ0+etL82v/jiC33yySf2m9o//fRTPf/88/r2228LVJPZCCAO4ObmphUrVmjatGlKSEjQoUOH9M0336h27doaMGCArly5otdff13x8fHat2+fXnvtNXl4eNinBRs3bqxt27bphx9+UGJiomJjY3X48OFc+yhbtqxOnDihCxcu5LuuVq1a6ZNPPlHDhg3l6uqqqlWrqnbt2vrqq6/Upk0b+7i+ffvqX//6l+bMmaPjx48rLi5OI0eOVFpamry8vO54fB4eHpIkV1dXHTt2TKmpqYVwRouH4tjXu/XK29tb6enp+sc//qEzZ85oy5Yt9mvWN8NSQkKCxo4dq7i4OJ0+fVr//Oc/debMGfvUsaurqy5duqTjx4/na8amJOndu7f+9a9/6f3339fx48f173//W++++65atWp1x19Wrq6uSk5OVmJiYr73FRERoU2bNun8+fNq0qSJJCk0NFRfffWV/f4s6ca0/eXLlzVs2DAdPHhQ8fHxGj58uPbt26dHHnlEFSpU0MaNGzVmzBgdPHhQiYmJWrFihUqVKqUGDRpIuvH/2enTp5WUlHQPZ+f+ZFZP79anSpUqycnJSf/4xz+UmJio/fv3a8iQITp//rz9tZmRkaGpU6dq3bp1OnXqlHbv3q2dO3fmem1KUnx8vK5evXqPZ6bwEUAcoG7dupozZ462b9+ujh07qlu3bnJyctLChQtVs2ZN/f3vf1daWpq6du2q3r17y8vLS5988onc3d0lST169FDbtm0VHR2tTp066cKFC+rRo0eufXTv3l0bN25Ur1698l1X69atlZmZqZCQEPuy0NBQGYahVq1a2Zc9+eSTmjlzpr7//nt16NBBr7/+ukJDQzV37ty7Ht/Na8y9evXS8uXLNWrUqIKexmKnOPb1br168skn1bt3b02dOlVPPfWUJk2apOeee05NmzbVvn37JEnjx49XaGiooqOj1bZtW/u/yG7exPfEE0/Iy8tLzzzzjA4cOFBIZ/P+8NRTTykmJkb//Oc/1aFDB40dO1bt2rWzvx32djp27Kj09HS1b99eycnJ+dpXo0aNVLZsWT366KP26f/Q0FDl5OSodevW9nE1a9bU8uXLlZ6erm7duikqKkoWi0XLli1TxYoVc70We/TooXbt2mn79u1asGCBatWqJUn6y1/+osOHD+uZZ56xX354UJjV07v1qUqVKpoyZYp++OEHPf3003rttddUpUoV9ejRQ/v375dhGPrzn/+sQYMGad68eXrqqac0ZMgQhYWFacyYMZJuzOaEh4dryJAhWrVqVWGcnkJlMf73ojMAAEARYwYEAACYjgACAABMRwABAACmI4AAAADTEUAAAIDpCCAAAMB0BBAAAGA6AgiA+1L37t3VvXt3R5cBoID4IDIA96WjR49KuvEJtADuPwQQAABgOqe7DwGAgomIiFCbNm106NAh7d+/X+3bt9ewYcM0Y8YMbdiwQZcvX1a9evU0dOhQhYaG2p935coVvffee1q/fr2uX7+uli1bKigoSJMnT9ahQ4ckyX755e9//7ukG3+Ya9GiRfrqq690+vRpVa1aVc8995z69Olj/xtE3bt3V61atfTQQw9pxYoVSklJUf369TVy5EgFBQWZfHaABxsBBECR+vjjj/Xiiy/qlVdekYuLi15++WVduHBBQ4cOVeXKlbV69Wr16dNHixYtsoeQgQMH6sCBAxo6dKiqVaumFStWaPr06bfdh2EY6t+/v/bu3auBAweqXr162rFjh2bNmqXExES9++679rHfffedfHx8NGbMGBmGoalTp2rw4MH64YcfZLPZivx8ALiBAAKgSFWuXFkjRoyQ1WrVp59+qvj4eH366af2GYcWLVqoe/fuiomJ0erVqxUXF6ft27drzpw5euKJJ+xjOnToYL/v439t3rxZ27Zt07Rp0/TMM89Ikpo3by4XFxfNnj1bL7/8sv1ekaysLC1evFhubm6SpKtXr+rNN9/UwYMH7X+OHkDR410wAIqUj4+P/RJIXFycvLy8VL9+fWVlZSkrK0vZ2dlq1aqVfv75Z126dEnbt29XqVKl1KZNG/s2rFarnnrqqdvuY+fOnbLZbHr66adzLb8ZRnbs2GFfVrduXXv4kKQqVapIktLT0+/9YAHkGzMgAIpUpUqV7N9fvHhR58+fV/369fMce/78eaWmpqpChQr20JLXdv7XpUuX5OHhISen3D/SvLy8JEmXL1+2LytTpkyuMTf3k5OTk4+jAVBYCCAATFOuXDnVrl1bMTExea6vUaOGqlSpotTUVOXk5OQKISkpKbfdbvny5ZWamqqsrKxcISQ5OVmS5OHhUUhHAKCwcAkGgGn+9Kc/6ezZs6pYsaICAwPtX3FxcVq0aJFsNpv+9Kc/KSsrSz/88EOu527YsOGO283Ozta3336ba/mXX34pSWrSpEnhHwyAe8IMCADTdO7cWcuXL1fPnj3Vv39/Va1aVdu2bdPChQsVFRWlUqVKqWnTpmrevLlGjx6tCxcuqFq1avr8888VHx8vi8WS53ZbtGihZs2aaezYsUpOTlZAQIB27typhQsXqlOnTnxYGVAMEUAAmMbV1VUff/yxpk+frmnTpuny5cuqXr26hg8frl69etnHzZw5U1OmTNH06dOVlZWl1q1b64UXXtC6devy3K7FYtGHH36o2NhY/e1vf9Ovv/6qGjVqaOjQoerZs6dJRwfgj+CTUAEUK6dPn9bevXvVunVrubi42JcPHjxYiYmJWrt2rQOrA1BYmAEBUKxYrVaNGDFCrVu31nPPPSebzabNmzfrX//6lyZPnuzo8gAUEmZAABQ727dv1/vvv6+DBw8qKytLPj4+6tmzp9q3b+/o0gAUEgIIAAAwHW/DBQAApiOAAAAA0xFAAACA6QggAADAdAQQAABgOgIIAAAwHQEEAACYjgACAABMRwABAACm+3+hVsbrZSw0wQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'region' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.countplot(x='region',data=Insurance_Data, hue='region', palette='viridis', legend=False )\n",
    "plt.title('Region Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6fe4ac3a-e6ea-43cf-8b21-66b32bbbd6b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "region\n",
       "southeast    364\n",
       "southwest    325\n",
       "northwest    325\n",
       "northeast    324\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Displaying the count of each category in the 'region' column\n",
    "Insurance_Data['region'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "2f37683d-0fb4-4d2e-8069-f8c4176afe1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_7868\\2522413577.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(Insurance_Data['charges'])\n"
     ]
    },
    {
     "data": {
      "image/png": "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x2PatGnev993333o3LkzXnzxRQiCAABISEjA/PnzveesX78ehw8fxgcffIA+ffoAAEaMGIEZM2bg2Wefxccff4wDBw7AYrHg9ttvR0pKCgCgRYsW+Pbbb1FZWYmoqKgm/CoShR+GB6Iwtm/fPtjtdowbN67a8YULF3r/jIuL8wYHAGjTpg0AoKysDABw9dVX4+qrr4bVakVWVhZOnjyJgwcPwul0wm63V7tuly5dvP9ts9mwd+9e3Hnnnd7gAAATJkyAWn3un6Zt27YhKSkJPXv2hMPh8B4fPXo0nn76aZSWlqJPnz7Q6XSYNm0aJk6ciJEjR6J///5IS0tr7JeIiGrA8EAUxkpKSgAA8fHxtZ4TERFR7e+eD3rPfAaLxYJly5Zh/fr1cDgcaN26NdLT06FWq3HhqGhiYmK193Y6nUhISKh2jlqtRlxcXLXzCgoK0LNnzxrrKygoQOfOnfHWW2/h1VdfxQcffIA33ngDRqMRN9xwA+6++24OWxAFGMMDURgzGo0AgKKiInTs2NF7/MyZMzh58uRFPQc1eeyxx/DVV1/h+eefx9ChQ71hY8iQIXW+LiEhARqNBoWFhdWOu1wuFBcXe/8eHR2N9u3b49lnn63xOq1btwYApKWl4cUXX4TNZsPu3bvx/vvvY9WqVejatSsmTpxYbzuIyHeM40RhLC0tDRqNBt9++2214//9739x9913VxtOqM3u3bsxaNAgXH755d7g8Pvvv6OoqMjbO1ETlUqFfv36YfPmzdWOf/fdd9WGJwYOHIgzZ84gISEBvXv39j62bduG119/HSqVCm+88QbGjBkDm80GrVaLIUOGYNmyZQDcQYiIAos9D0RhLD4+HjfffDP++9//QqvVYvDgwfjtt9/w1ltvYf78+Th69Gi910hLS8MXX3yBd999F506dcLhw4fxyiuvQBAEmM3mOl87b948zJgxA/PmzcO0adNw+vRpvPDCCwDODY9MnToVb731FmbNmoU77rgDLVq0wC+//ILXXnsNN910EzQaDQYPHoxnn30Wd955J2666SaoVCq899570Gq1GD16dOO/UERUDcMDUZi77777kJiYiHfffRdr1qxB69at8dBDD+GGG27wTpysy8KFC2G32/H888/DZrOhdevWmDNnDjIyMvDdd9/B6XTW+tr+/ftj5cqVeOGFFzB37ly0atUKjzzyCP75z38iMjISgHvOxdtvv43ly5fjmWeeQVlZGVq1aoV7770Xs2fPBgB069YNq1atwksvvYT58+fD6XSiV69eWLNmTbXhGCIKDO7zQESy+fbbb5GamlptMuSff/6JyZMn4+WXX8bYsWNlrI6IasOeByKSzdatW/H5559jwYIF6NChA3Jzc/HKK6+gY8eOuOyyy+Quj4hqwZ4HIpKNxWLBCy+8gK+++gr5+fmIjY3F8OHDce+991Zb1klEwYXhgYiIiPzCpZpERETkF4YHIiIi8gvDAxEREfmF4YGIiIj8wvBAREREfmF4ICIiIr8wPBAREZFfGB6IiIjILwwPRERE5Jf/D4618y2ynC+FAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Visualizing the distribution of the 'charges' column\n",
    "plt.figure(figsize=(6,6))\n",
    "sns.distplot(Insurance_Data['charges'])\n",
    "plt.title('Charges Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b177cde-e8da-4957-9207-5fdbe38b2871",
   "metadata": {},
   "source": [
    "Data Pre-processing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "824dba71-4828-49d7-be3c-99c1bc3d3616",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Encoding the categorical features\n",
    "# Sex column\n",
    "Insurance_Data['sex'] = Insurance_Data['sex'].replace({'male': 0, 'female': 1}).astype(int)\n",
    "\n",
    "# Smoker column\n",
    "Insurance_Data['smoker'] = Insurance_Data['smoker'].replace({'yes': 0, 'no': 1}).astype(int)\n",
    "\n",
    "# Region column\n",
    "Insurance_Data['region'] = Insurance_Data['region'].replace({'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}).astype(int)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "babf76c9-59bb-48b9-af41-c5919ea2480a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      age  sex     bmi  children  smoker  region      charges\n",
      "0      19    1  27.900         0       0       1  16884.92400\n",
      "1      18    0  33.770         1       1       0   1725.55230\n",
      "2      28    0  33.000         3       1       0   4449.46200\n",
      "3      33    0  22.705         0       1       3  21984.47061\n",
      "4      32    0  28.880         0       1       3   3866.85520\n",
      "...   ...  ...     ...       ...     ...     ...          ...\n",
      "1333   50    0  30.970         3       1       3  10600.54830\n",
      "1334   18    1  31.920         0       1       2   2205.98080\n",
      "1335   18    1  36.850         0       1       0   1629.83350\n",
      "1336   21    1  25.800         0       1       1   2007.94500\n",
      "1337   61    1  29.070         0       0       3  29141.36030\n",
      "\n",
      "[1338 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "print(Insurance_Data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "083c18f8-035b-49ff-940b-8dd6098ffb72",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Splitting the features and targets\n",
    "X = Insurance_Data.drop(columns='charges', axis=1)\n",
    "Y = Insurance_Data['charges']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c2906cc2-7a46-4ab1-9f74-a6178009db0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      age  sex     bmi  children  smoker  region\n",
      "0      19    1  27.900         0       0       1\n",
      "1      18    0  33.770         1       1       0\n",
      "2      28    0  33.000         3       1       0\n",
      "3      33    0  22.705         0       1       3\n",
      "4      32    0  28.880         0       1       3\n",
      "...   ...  ...     ...       ...     ...     ...\n",
      "1333   50    0  30.970         3       1       3\n",
      "1334   18    1  31.920         0       1       2\n",
      "1335   18    1  36.850         0       1       0\n",
      "1336   21    1  25.800         0       1       1\n",
      "1337   61    1  29.070         0       0       3\n",
      "\n",
      "[1338 rows x 6 columns]\n",
      "0       16884.92400\n",
      "1        1725.55230\n",
      "2        4449.46200\n",
      "3       21984.47061\n",
      "4        3866.85520\n",
      "           ...     \n",
      "1333    10600.54830\n",
      "1334     2205.98080\n",
      "1335     1629.83350\n",
      "1336     2007.94500\n",
      "1337    29141.36030\n",
      "Name: charges, Length: 1338, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(X)\n",
    "print(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "8cfd2a55-2833-4bb0-a6c1-596ce1a621c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# splitting the data into training and testing data\n",
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state =2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f285cb57-7f78-4a05-943c-57fb548fac54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1338, 6) (1070, 6) (268, 6)\n"
     ]
    }
   ],
   "source": [
    "print(X.shape, X_train.shape, X_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "72c15549-ad1a-45bd-9dd7-9ddc7057acc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model training\n",
    "# Linear Regression \n",
    "regressor=LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "3242e85e-2ea7-4bcb-b2a1-f75440da9f6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-1 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-1 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-1 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-1 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-1 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;&nbsp;LinearRegression<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.LinearRegression.html\">?<span>Documentation for LinearRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>LinearRegression()</pre></div> </div></div></div></div>"
      ],
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regressor.fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b8ab0f14-2edd-438f-ae21-383193f79533",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model evaluation\n",
    "# prediction on training data\n",
    "training_data_prediction = regressor.predict(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "c8e2678a-c4d7-42ca-bd97-ef579e221819",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "R Squared Value :  0.751505643411174\n"
     ]
    }
   ],
   "source": [
    "# R squared value \n",
    "r2_train = metrics.r2_score(Y_train, training_data_prediction)\n",
    "print('R Squared Value : ', r2_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "49fcd9e6-a48d-4732-bd57-aeb62da6c2c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# prediction on training data\n",
    "testing_data_prediction = regressor.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "1ff2d9a4-a3a0-4fd4-a1d0-382096f3fee3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "R Squared Value :  0.7447273869684077\n"
     ]
    }
   ],
   "source": [
    "# R squared value \n",
    "r2_test = metrics.r2_score(Y_test, testing_data_prediction)\n",
    "print('R Squared Value : ', r2_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "cf0c44ff-ad71-4a7b-9e1a-ba446bef9a2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3760.0805765]\n",
      "The Insurance cost is USD  3760.0805764960496\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\anaconda3\\Lib\\site-packages\\sklearn\\base.py:493: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "# Building the predictive system\n",
    "# Defining a sample input tuple (age, sex, bmi, children, smoker, region)\n",
    "input_data = (31,1,25.74,0,1,0)\n",
    "\n",
    "# changing input data to a numpy array\n",
    "input_data_as_nparray = np.asarray(input_data)\n",
    "\n",
    "#reshape the arrray\n",
    "input_data_reshaped= input_data_as_nparray.reshape(1,-1)\n",
    "\n",
    "# Making a prediction using the trained model\n",
    "prediction = regressor.predict(input_data_reshaped)\n",
    "print(prediction)\n",
    "\n",
    "print('The Insurance cost is USD ', prediction[0])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b215c283-87b8-4957-95c6-76e263a2387f",
   "metadata": {},
   "source": [
    "Conclusion\n",
    "\n",
    "The Insurance Cost Prediction project successfully demonstrates the application of Linear Regression to solve a real-world problem: predicting insurance costs based on demographic and health-related factors. By analyzing and preprocessing the data, visualizing key patterns, and building a predictive model, the project highlights the following key takeaways:\n",
    "\n",
    "Key Insights:\n",
    "\n",
    "Features such as age, BMI, smoking status, and number of children significantly impact insurance charges.\n",
    "Smokers are more likely to incur higher insurance costs compared to non-smokers, as seen in the visualizations and model predictions.\n",
    "Model Performance:\n",
    "\n",
    "The Linear Regression model performed well, achieving a satisfactory R-squared score on both training and testing datasets, indicating that the model explains a substantial portion of the variance in the target variable (insurance charges).\n",
    "Business Impact:\n",
    "\n",
    "This predictive system can help insurance companies assess premiums more accurately, leading to better risk assessment and pricing strategies.\n",
    "Individuals can also gain insights into how lifestyle choices (e.g., quitting smoking or managing BMI) might influence their insurance costs.\n",
    "Learning Outcomes:\n",
    "\n",
    "This project provided hands-on experience in:\n",
    "Data preprocessing, visualization, and feature encoding.\n",
    "Applying machine learning techniques for regression tasks.\n",
    "Building an end-to-end predictive pipeline for real-world applications.\n",
    "Future Improvements:\n",
    "\n",
    "Incorporating more features, such as occupation, medical history, or physical activity levels, to improve prediction accuracy.\n",
    "Exploring advanced machine learning models like Random Forest, Gradient Boosting, or Deep Learning for potentially better performance.\n",
    "Deploying the predictive system using web frameworks like Flask or Streamlit for user-friendly interaction.\n",
    "This project underscores the power of data-driven decision-making and showcases how machine learning can be applied to solve complex problems in the insurance industry and beyond."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
