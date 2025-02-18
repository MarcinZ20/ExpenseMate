import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import { useAuthStore } from './auth'
import { Transaction } from '@/models/Transaction'



export const useTransactionStore = defineStore('transactions', {
    state: () => ({
        transactions: [] as Transaction[]
    }), 
    actions: {
        async getUserTransactions(user_id: number, page: number = 1, page_size: number = 10) {
            const auth = useAuthStore()

            if (!auth.isAuthenticated) {
                console.error('You have be logged in to access transactions')
                return 
            }
            try {
                const response = await axios.get(
                    `http://localhost:8000/api/users/${user_id}/transactions/?page=${page}&page_size=${page_size}`,
                    {
                        headers: {
                            'Accept': 'application/json;version=1.0',
                            Authorization: `Bearer ${auth.token}`
                        }
                    }
                )
                
                this.transactions = response.data.results.map(
                    (t: any) => new Transaction(t.id, t.user, t.type, t.category, t.amount, t.description, t.date, t.time)
                )

                this.transactions.sort((t1: Transaction, t2: Transaction) => {
                    if (t1.date > t2.date) return 1
                    if (t2.date > t1.date) return -1
                    return 0
                })
            } catch (error) {
                console.error('Error while fetching transactions: ', error)
            }
        }
    },
    getters: {
        Latest: (state) => (number: number = 3) => {
            return state.transactions.slice(0, Math.min(number, state.transactions.length))
        },
        MonthlyIncomeTotal: (state) => {
            return state.transactions
                .filter((t: Transaction) => t.type === 'income')
                .reduce((sum, t: Transaction) => sum + (t.amount ?? 0), 0)
        },
        MonthlyExpenseTotal: (state) => {
            return state.transactions
                .filter((t: Transaction) => t.type === 'expense')
                .reduce((sum, t: Transaction) => sum + (t.amount ?? 0), 0)
        },
        lastMonthExpenses: (state) => {
            let date = new Date()
            date.setDate(date.getDate() - 30)

            return state.transactions
                .filter((t: Transaction) => t.date >= date && t.type === 'expense')
                .sort((t1: Transaction, t2: Transaction) => {
                    return t1.date < t2.date ? 1 : t1.date > t2.date ? -1 : 0
                })
        },
        chartExpenses: (state) => {
            let expenses = state.transactions
                .filter((t: Transaction) => t.type === 'expense')
                .map((t: Transaction) => [t.date.getTime(), t.amount])
            console.log(expenses)
            return expenses
        },
        chartIncome: (state) => {
            return state.transactions
                .filter((t: Transaction) => t.type === 'income')
                .map((t: Transaction) => [t.date.getTime(), t.amount])
        }
    }
})