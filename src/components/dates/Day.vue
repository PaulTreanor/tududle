<template>
    <div>
        <div class="day" v-bind:class="{'greyedout':day==-1, 'redout':day==0}" >
            <h2 >{{thisWeekday()}}</h2>
        
            <p class="date">{{thisDate()}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "Day",
    props: ["day"],
    data() {
        return {
            monthNames : ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"],
            days: ["yesterday", "today", "tomorrow", "dayAfterTomorrow", "twoDaysFromNow"],
            weekdays : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            //today : new Date(),
            today : ( d => new Date(d.setDate(d.getDate() +this.day)) )(new Date)
           
            
            
        }
    },
    methods : {
        thisWeekday() {            
            return this.weekdays[this.today.getDay() -1];
            
        },
        thisDate() {
            var thisMonth = this.monthNames[this.today.getMonth()];
            var thisDay = this.today.getDate();
            var thisYear = this.today.getFullYear();
            return thisDay + " " + thisMonth + ", " + thisYear;
        }    
    }
}
</script>

<style scoped>
.day {
	margin: auto;
	text-align: center;
	font-family: 'Oswald', "Helvetica Neue", Helvetica, Arial sans-serif;
	text-transform: uppercase;
	}

p {
	margin:auto;
	text-align: center;
	padding-bottom: 20px;
}
.greyedout {
    color: #888 !important;
}

.redout {
    color: red;
}
</style>